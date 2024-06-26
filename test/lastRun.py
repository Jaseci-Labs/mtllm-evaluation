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
    df.to_csv("ModelSweep-25-06-2024-2249.csv")


ds = load_dataset("openai/gsm8k", "main", split="train")
train = ds.iter(batch_size=1)
res = []
count = 0
for i in train:
    if (count == 300):
        exit(0)
    question = i["question"][0]
    answer_str: str = i["answer"][0]
    answer = answer_str.split(" ")[-1].replace(",", "")
    for model in models:
        print(f"Running Question {count} with model {model}")

        # dspyFailed = False
        # jacFailed = False
        # dspyRawPrompt = ""
        # jacRawPrompt = ""
        # try:
        #     dspyResponse, dspyTimer = codeRun(
        #         ["python", "tested_code/gsm8k/dspy_single_trial.py"], input=question, modelName=model
        #     )
        #     dspyResponse = dspyResponse.strip()
        # except KeyboardInterrupt:
        #     exit(1)
        # except:
        #     dspyFailed = True
        #     dspyResponse = ""
        #     dspyTimer = 0
        #     print(dspyRawPrompt)
        # with open("RawPrompt.json", "r") as rawPromptFile, open("RawResponse.json", "r") as rawResponseFile:
        #     dspyRawPrompt = rawPromptFile.read()
        #     dspyRawResponse = json.load(rawResponseFile)
        # os.remove("RawPrompt.json")
        # os.remove("RawResponse.json")
        # dspyPromptTokens = sum([i["usage"]["prompt_tokens"] for i in dspyRawResponse])
        # dspyCompletionTokens = sum([i["usage"]["completion_tokens"] for i in dspyRawResponse])
        # dspyResult = [count, question, answer, model, "DSPy_Single_Trial", dspyResponse, (dspyResponse == answer), dspyFailed, dspyTimer, dspyPromptTokens, dspyCompletionTokens, dspyRawPrompt, json.dumps(dspyRawResponse)]
        # print("DSPy Result", dspyResult)
        # res.append(dspyResult.copy())



        dspyFailed = False
        jacFailed = False
        dspyRawPrompt = ""
        jacRawPrompt = ""
        try:
            dspyResponse, dspyTimer = codeRun(
                ["python", "tested_code/gsm8k/dspy_compiled_impl.py"], input=question, modelName=model
            )
            dspyResponse = dspyResponse.strip()
        except KeyboardInterrupt:
            exit(1)
        except:
            dspyFailed = True
            dspyResponse = ""
            dspyTimer = 0
            print(dspyRawPrompt)
        with open("RawPrompt.json", "r") as rawPromptFile, open("RawResponse.json", "r") as rawResponseFile:
            dspyRawPrompt = rawPromptFile.read()
            dspyRawResponse = json.load(rawResponseFile)
        os.remove("RawPrompt.json")
        os.remove("RawResponse.json")
        dspyPromptTokens = sum([i["usage"]["prompt_tokens"] for i in dspyRawResponse])
        dspyCompletionTokens = sum([i["usage"]["completion_tokens"] for i in dspyRawResponse])
        dspyResult = [count, question, answer, model, "DSPy_Compiled", dspyResponse, (dspyResponse == answer), dspyFailed, dspyTimer, dspyPromptTokens, dspyCompletionTokens, dspyRawPrompt, json.dumps(dspyRawResponse)]
        print("DSPy Result", dspyResult)
        res.append(dspyResult.copy())


    save(res)
    count += 1
