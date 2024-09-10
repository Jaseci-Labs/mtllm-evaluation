from datetime import datetime
import os
from datasets import load_dataset
import subprocess
import pandas as pd
import json

models = ["gpt-3.5-turbo", "gpt-4", "gpt-4-turbo", "gpt-4o"]
# models = ["gpt-4o"]


def codeRun(cmd: list[str], input: str, modelName: str):
    subEnv = os.environ.copy()
    subEnv["MODEL_NAME"] = modelName
    with open("/tmp/STDIN.txt", "w") as inputFile:
        inputFile.write(input)
    with open("/tmp/STDIN.txt", "r") as inputFile:
        start = datetime.now()
        res = subprocess.check_output(cmd, stdin=inputFile, env=subEnv).decode()
        duration = datetime.now() - start
        return res, duration.total_seconds()


def save(res):
    df = pd.DataFrame(
        res,
        columns=[
            "QuestionID",
            "Question",
            "GivenAnswer",
            "Model",
            "Program",
            "Output",
            "ExactMatch",
            "Failed",
            "Time(s)",
            "PromptTokens",
            "CompletionTokens",
            "RawPrompt",
            "RawResponse",
        ],
    )
    df.to_csv("ModelSweep-19-06-2024-1820.csv")


ds = load_dataset("openai/gsm8k", "main", split="train")
train = ds.iter(batch_size=1)
res = []
count = 0
for i in train:
    if count == 300:
        exit(0)
    question = i["question"][0]
    answer_str: str = i["answer"][0]
    answer = answer_str.split(" ")[-1].replace(",", "")
    for model in models:
        print(f"Running Question {count} with model {model}")
        dspyFailed = False
        jacFailed = False
        dspyRawPrompt = ""
        jacRawPrompt = ""
        try:
            dspyResponse, dspyTimer = codeRun(
                ["python", "tested_code/gsm8k/dspy_compiled_impl.py"],
                input=question,
                modelName=model,
            )
            dspyResponse = dspyResponse.strip()
        except KeyboardInterrupt:
            exit(1)
        except:
            dspyFailed = True
            dspyResponse = ""
            dspyTimer = 0
            print(dspyRawPrompt)
        with open("RawPrompt.txt", "r") as rawPromptFile, open(
            "RawResponse.json", "r"
        ) as rawResponseFile:
            dspyRawPrompt = rawPromptFile.read()
            dspyRawResponse = json.load(rawResponseFile)
        os.remove("RawPrompt.txt")
        os.remove("RawResponse.json")
        dspyResult = [
            count,
            question,
            answer,
            model,
            "DSPy",
            dspyResponse,
            (dspyResponse == answer),
            dspyFailed,
            dspyTimer,
            dspyRawResponse["usage"]["prompt_tokens"],
            dspyRawResponse["usage"]["completion_tokens"],
            dspyRawPrompt,
            json.dumps(dspyRawResponse),
        ]
        print("DSPy Result", dspyResult)
        res.append(dspyResult)

        try:
            jacResponse, jacTimer = codeRun(
                ["jac", "run", "tested_code/gsm8k/jac_impl.jac"],
                input=question,
                modelName=model,
            )
            jacResponse = jacResponse.strip()
        except KeyboardInterrupt:
            exit(1)
        except:
            jacFailed = True
            jacResponse = ""
            jacTimer = 0
        with open("RawPrompt.txt", "r") as rawPromptFile, open(
            "RawResponse.json", "r"
        ) as rawResponseFile:
            jacRawPrompt = rawPromptFile.read()
            jacRawResponse = json.load(rawResponseFile)
        os.remove("RawPrompt.txt")
        os.remove("RawResponse.json")
        jacResult = [
            count,
            question,
            answer,
            model,
            "Jac",
            jacResponse,
            (jacResponse == answer),
            jacFailed,
            jacTimer,
            jacRawResponse["usage"]["prompt_tokens"],
            jacRawResponse["usage"]["completion_tokens"],
            jacRawPrompt,
            json.dumps(jacRawResponse),
        ]
        print("Jac Result", jacResult)
        res.append(jacResult)

    save(res)
    count += 1
