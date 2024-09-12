from datetime import datetime
import os
from datasets import load_dataset
import subprocess
import pandas as pd
import json

models = ["llama2", "llama3", "llama3.1"]
# models = ["gpt-4o"]


def codeRun(cmd: list[str], input: str, modelName: str):
    subEnv = os.environ.copy()
    subEnv["MODEL_NAME"] = modelName
    print(modelName)
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
    df.to_csv("ModelSweep-11-09-2024-2352.csv")


def sumToken(key: str, response):
    sum = 0
    for res in response:
        sum += res["usage"][key]
    return sum

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
                ["python", "tested_code/gsm8k/dspy_llama_single_trial.py"],
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
        with open("/tmp/RawPrompt.txt", "r") as rawPromptFile, open(
            "/tmp/RawResponse.json", "r"
        ) as rawResponseFile:
            dspyRawPrompt = rawPromptFile.read()
            dspyRawResponse = json.load(rawResponseFile)
        os.remove("/tmp/RawPrompt.txt")
        os.remove("/tmp/RawResponse.json")
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
            sumToken("prompt_tokens", dspyRawResponse),
            sumToken("completion_tokens", dspyRawResponse),
            # dspyRawResponse["usage"]["prompt_tokens"],
            # dspyRawResponse["usage"]["completion_tokens"],
            dspyRawPrompt,
            json.dumps(dspyRawResponse),
        ]
        print("DSPy Result", dspyResult)
        res.append(dspyResult)

        try:
            jacResponse, jacTimer = codeRun(
                ["jac", "run", "tested_code/gsm8k/jac_llama_impl.jac"],
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
        with open("/tmp/RawPrompt.txt", "r") as rawPromptFile, open(
            "/tmp/RawResponse.json", "r"
        ) as rawResponseFile:
            jacRawPrompt = rawPromptFile.read()
            jacRawResponse = json.load(rawResponseFile)
        os.remove("/tmp/RawPrompt.txt")
        os.remove("/tmp/RawResponse.json")
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
            sumToken("prompt_tokens", jacRawResponse),
            sumToken("completion_tokens", jacRawResponse),
            # jacRawResponse["usage"]["prompt_tokens"],
            # jacRawResponse["usage"]["completion_tokens"],
            jacRawPrompt,
            json.dumps(jacRawResponse),
        ]
        print("Jac Result", jacResult)
        res.append(jacResult)

    save(res)
    count += 1
