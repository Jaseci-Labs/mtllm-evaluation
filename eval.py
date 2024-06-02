import os
from pyinstrument import Profiler
from pyinstrument.renderers import JSONRenderer
from cProfile import Profile
import importlib
from jaclang import jac_import
from loguru import logger
import json
import sys
import argparse


def run_dspy_program(program_name, program_path, profiler):
    os.makedirs(f"results/{program_name}/dspy", exist_ok=True)
    program_path = program_path.replace(".py", "").replace("/", ".")

    results_file = open(f"results/{program_name}/dspy/results.txt", "w")
    sys.stdout = results_file

    if profiler == "cProfile":
        pr = Profile()
        pr.enable()
    else:
        profiler = Profiler()
        profiler.start()

    module = importlib.import_module(program_path)

    if profiler == "cProfile":
        pr.disable()
        pr.dump_stats(f"results/{program_name}/dspy/profile.prof")
    else:
        profiler.stop()
        with open(f"results/{program_name}/dspy/profile.html", "w") as f:
            f.write(profiler.output_html())
        with open(f"results/{program_name}/dspy/profile.json", "w") as f:
            json.dump(json.loads(profiler.output(JSONRenderer())), f, indent=4)

    sys.stdout = sys.__stdout__
    results_file.close()


def run_jac_program(program_name, program_path, profiler):
    os.makedirs(f"results/{program_name}/jac", exist_ok=True)
    program_path = os.path.abspath(program_path)
    program_dir, program_file = os.path.split(program_path)

    results_file = open(f"results/{program_name}/jac/results.txt", "w")
    sys.stdout = results_file

    if profiler == "cProfile":
        pr = Profile()
        pr.enable()
    else:
        profiler = Profiler()
        profiler.start()

    module = jac_import(program_file.replace(".jac", ""), base_path=program_dir)

    if profiler == "cProfile":
        pr.disable()
        pr.dump_stats(f"results/{program_name}/jac/profile.prof")
    else:
        profiler.stop()
        with open(f"results/{program_name}/jac/profile.html", "w") as f:
            f.write(profiler.output_html())
        with open(f"results/{program_name}/jac/profile.json", "w") as f:
            json.dump(json.loads(profiler.output(JSONRenderer())), f, indent=4)

    sys.stdout = sys.__stdout__
    results_file.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--profiler",
        help="Which profiler to use",
        default="cProfile",
        type=str,
        choices=["cProfile", "pyinstrument"],
    )
    parser.add_argument(
        "--config",
        help="Location to the Eval config",
        default="eval.config.json",
        type=str,
    )
    args = parser.parse_args()
    logger.info(f"Using {args.profiler} as the profiler.")
    with open(args.config) as f:
        EVAL_PROBLEMS = json.load(f)
    for difficulty, PROBLEM_SET in EVAL_PROBLEMS.items():
        for problem_name, paths in PROBLEM_SET.items():
            logger.info(f"Running {problem_name} problem from {difficulty} difficulty.")

            logger.info(f"Running JAC program: {paths['jac']}")
            run_jac_program(problem_name, paths["jac"], args.profiler)

            logger.info(f"Running Dspy program: {paths['dspy']}")
            run_dspy_program(problem_name, paths["dspy"], args.profiler)
