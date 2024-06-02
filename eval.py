import os
from pyinstrument import Profiler
import importlib
from jaclang import jac_import
from loguru import logger
import json
import sys


def run_dspy_program(program_name, program_path):
    os.makedirs(f"results/{program_name}/dspy", exist_ok=True)
    program_path = program_path.replace(".py", "").replace("/", ".")

    results_file = open(f"results/{program_name}/dspy/results.txt", "w")
    sys.stdout = results_file

    profiler = Profiler()
    profiler.start()

    module = importlib.import_module(program_path)

    profiler.stop()
    with open(f"results/{program_name}/dspy/profile.txt", "w") as f:
        f.write(profiler.output_text())

    sys.stdout = sys.__stdout__
    results_file.close()


def run_jac_program(program_name, program_path):
    os.makedirs(f"results/{program_name}/jac", exist_ok=True)
    program_path = os.path.abspath(program_path)
    program_dir, program_file = os.path.split(program_path)

    results_file = open(f"results/{program_name}/jac/results.txt", "w")
    sys.stdout = results_file

    profiler = Profiler()
    profiler.start()

    module = jac_import(program_file.replace(".jac", ""), base_path=program_dir)

    profiler.stop()
    with open(f"results/{program_name}/jac/profile.txt", "w") as f:
        f.write(profiler.output_text())

    sys.stdout = sys.__stdout__
    results_file.close()


if __name__ == "__main__":
    with open("eval.config.json") as f:
        EVAL_PROBLEMS = json.load(f)
    for difficulty, PROBLEM_SET in EVAL_PROBLEMS.items():
        for problem_name, paths in PROBLEM_SET.items():
            logger.info(f"Running {problem_name} problem from {difficulty} difficulty.")

            logger.info(f"Running JAC program: {paths['jac']}")
            run_jac_program(problem_name, paths["jac"])

            logger.info(f"Running Dspy program: {paths['dspy']}")
            run_dspy_program(problem_name, paths["dspy"])
