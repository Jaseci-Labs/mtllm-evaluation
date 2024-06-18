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
import time


def run_dspy_program(program_name, program_path, profiler, output_dir):
    os.makedirs(f"{output_dir}/{program_name}/dspy", exist_ok=True)
    program_path = program_path.replace(".py", "").replace("/", ".")

    results_file = open(f"{output_dir}/{program_name}/dspy/results.txt", "w")
    sys.stdout = results_file

    if profiler == "cProfile":
        pr = Profile()
        pr.enable()
    else:
        profiler = Profiler()
        profiler.start()

    try:
        module = importlib.import_module(program_path)
    except Exception as e:
        logger.error(f"Error while running {program_path}: {e}")

    if profiler == "cProfile":
        pr.disable()
        pr.dump_stats(f"{output_dir}/{program_name}/dspy/profile.prof")
    else:
        profiler.stop()
        with open(f"{output_dir}/{program_name}/dspy/profile.html", "w") as f:
            f.write(profiler.output_html())
        with open(f"{output_dir}/{program_name}/dspy/profile.json", "w") as f:
            json.dump(json.loads(profiler.output(JSONRenderer())), f, indent=4)

    sys.stdout = sys.__stdout__
    results_file.close()


def run_jac_program(program_name, program_path, profiler, output_dir):
    os.makedirs(f"{output_dir}/{program_name}/jac", exist_ok=True)
    program_path = os.path.abspath(program_path)
    program_dir, program_file = os.path.split(program_path)

    results_file = open(f"{output_dir}/{program_name}/jac/results.txt", "w")
    sys.stdout = results_file

    if profiler == "cProfile":
        pr = Profile()
        pr.enable()
    else:
        profiler = Profiler()
        profiler.start()

    try:
        module = jac_import(program_file.replace(".jac", ""), base_path=program_dir)
    except Exception as e:
        logger.error(f"Error while running {program_path}: {e}")

    if profiler == "cProfile":
        pr.disable()
        pr.dump_stats(f"{output_dir}/{program_name}/jac/profile.prof")
    else:
        profiler.stop()
        with open(f"{output_dir}/{program_name}/jac/profile.html", "w") as f:
            f.write(profiler.output_html())
        with open(f"{output_dir}/{program_name}/jac/profile.json", "w") as f:
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
    parser.add_argument(
        "--output_dir",
        help="Output Directory Location",
        default="output",
        type=str,
    )
    args = parser.parse_args()
    logger.info(f"Using {args.profiler} as the profiler.")
    with open(args.config) as f:
        EVAL_PROBLEMS = json.load(f)
    if os.path.exists(args.output_dir):
        logger.info(f"Output directory exists. Do you want to overwrite it? (y/n)")
        if input().lower() != "y":
            logger.info("Exiting...")
            exit(0)
    for difficulty, PROBLEM_SET in EVAL_PROBLEMS.items():
        for problem_name, paths in PROBLEM_SET.items():
            if os.path.exists(f"{args.output_dir}/{problem_name}"):
                logger.info(f"Output directory for {problem_name} exists.")
                logger.info(f"Do you want to overwrite it? (y/n)")
                if input().lower() != "y":
                    logger.info("Skipping...")
                    continue

            logger.info(f"Running {problem_name} problem from {difficulty} difficulty.")

            logger.info(f"Running JAC program: {paths['jac']}")
            run_jac_program(problem_name, paths["jac"], args.profiler, args.output_dir)
            time.sleep(60)

            logger.info(f"Running Dspy program: {paths['dspy']}")
            run_dspy_program(
                problem_name, paths["dspy"], args.profiler, args.output_dir
            )
            time.sleep(60)
