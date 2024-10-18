from pprint import pprint

from datasets.arrow_dataset import tempfile
from testkit import AIEvaluator, FactEvaluator, RunnerEvaluator
from datasets import load_dataset
import subprocess
import pandas as pd
import numpy as np


def codeRun(cmd: list[str], input: str):
    with open("/tmp/STDIN.txt", "w") as inputFile:
        inputFile.write(input)
    with open("/tmp/STDIN.txt", "r") as inputFile:
        return subprocess.check_output(cmd, stdin=inputFile).decode()


def save(res):
    df = pd.DataFrame(
        res,
        columns=[
            "Question",
            "GivenAnswer",
            "DSPyCOTResponse",
            "JacRespose",
            "DSPyCOTExactMatch",
            "JacExactMatch",
            "DSPyCOTFailed",
            "JacFailed",
            "Exception",
        ],
    )
    df.to_csv("DSPyVanillaJacGSM8k.csv")


ds = load_dataset("openai/gsm8k", "main", split="train")
train = ds.iter(batch_size=1)
res = []
for i in train:
    question = i["question"][0]
    answer_str: str = i["answer"][0]
    dspyFailed = False
    jacFailed = False
    try:
        dspyResponse = codeRun(
            ["python", "tested_code/gsm8k/dspy_vanilla_impl.py"], input=question
        ).strip()
    except:
        dspyFailed = True
        dspyResponse = ""

    try:
        jacResponse = codeRun(
            ["jac", "run", "tested_code/gsm8k/jac_impl.jac"], input=question
        ).strip()
    except:
        jacFailed = True
        jacResponse = ""

    answer = answer_str.split(" ")[-1].replace(",", "")
    # print(question, answer)
    emEval = FactEvaluator(answer=answer)
    comparison = emEval.eval(dspyResponse, jacResponse)
    individual_test = [
        question,
        answer,
        dspyResponse,
        jacResponse,
        comparison.scoreA.overall(),
        comparison.scoreB.overall(),
        dspyFailed,
        jacFailed,
    ]
    print(individual_test)
    res.append(individual_test)
    if len(res) % 10 == 0:
        save(res)


# ds = load_dataset("hotpotqa/hotpot_qa", "fullwiki", split="train")
# train = ds.iter(batch_size=1)
# res = []
# print(ds)
# for i in train:
#     if i['level'][0] != 'hard':
#         continue
#     question = f"{i['context'][0]} {i['question'][0]}"
#     answer = i["answer"][0]
#     dspyResponse = codeRun(
#         ["python", "tested_code/qa/dspy_vanilla_impl.py"], input=question
#     ).strip()
#     jacResponse = codeRun(
#         ["jac", "run", "tested_code/qa/jac_impl.jac"], input=question
#     ).strip()
#     print(answer)
#     print("DSPy Response", dspyResponse)
#     print("JAC Response", jacResponse.strip())
#     emEval = FactEvaluator(answer=answer)
#     comparison = emEval.eval(dspyResponse, jacResponse)
#     print(comparison.scoreA, comparison.scoreB)
#     res.append(
#         [
#             question,
#             answer,
#             dspyResponse,
#             jacResponse,
#             comparison.scoreA.overall(),
#             comparison.scoreB.overall(),
#         ]
#     )
#     if len(res) % 10 == 0:
#         save(res)
# break
