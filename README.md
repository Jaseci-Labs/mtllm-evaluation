# MTLLM Evaluation

## Evaluation Methodology
We are evaluating a DSpy, LMQL and Jaclang's MTLLM Feature on problem set of different difficulty levels based on the
technique used and difficulty of the problem itself. There are 3 difficulty levels of problems:
- Easy
    - Problems that can be solved using simple prompt-based techniques. eg. `Translation`, `Summarization`
- Medium
    - Problems that require some level of understanding of the problem and the data. eg. `Text Classification`, `Named Entity Recognition`, `Question Answering`
- Hard
    - Problems that require a deep understanding of the problem and the data. eg. `Agents`, `Tool Usage`, `ReACT`

## Evaluation Metrics
We are evaluating DSpy, LMQL and Jaclang's MTLLM Feature on the following metrics:
- Overall Accuracy - The overall accuracy of the model on the problem set.
- Time Taken to Solve the Problem - The time taken to solve the problem.
- Readability of the Code - The readability of the code. (Human Evaluation)
- Number of Lines - The number of lines in the written.
- Token Usage - The number of tokens used by the LLMs.
- How Good it work good with different LLMs - The performance of the model on different LLMs.
    - OpenAI's GPT-3.5, GPT-4, GPT-4-turbo, GPT-4o
    - Anthrpic's Claude 3 (Sonnet, Opus)
    - Google's Gemini Models
    - OpenSource (LLama3 (8b, 70b), Mistral, Mixtral, Phi-3)

## Evaluation Results

### Easy Problems

| Problem Name | Methodology | Time Taken | Readability | Number of Lines | Token Usage | 
| ------------ | ----------- | ---------- | ----------- | --------------- | ----------- |
| Joke Generation | DSpy |  |  |  |  |  |
| | LMQL |  |  |  |  |  |
|  | Jaclang |  |  |  |  |  |
| Odd Word Out | DSpy |  |  |  |  |  |
|  | LMQL |  |  |  |  |  |
|  | Jaclang |  |  |  |  |  |
| Translation | DSpy |  |  |  |  |  |
|  | LMQL |  |  |  |  |  |
|  | Jaclang |  |  |  |  |  |
| Expert Answer | DSpy |  |  |  |  |  |
|  | LMQL |  |  |  |  |  |
|  | Jaclang |  |  |  |  |  |

### Medium Problems

| Problem Name | Methodology | Time Taken | Readability | Number of Lines | Token Usage | 
| ------------ | ----------- | ---------- | ----------- | --------------- | ----------- |
| MCQ Reasoning | DSpy |  |  |  |  |  |
| | LMQL |  |  |  |  |  |
|  | Jaclang |  |  |  |  |  |
| Text to Object | DSpy |  |  |  |  |  |
|  | LMQL |  |  |  |  |  |
|  | Jaclang |  |  |  |  |  |
| Object Filling | DSpy |  |  |  |  |  |
|  | LMQL |  |  |  |  |  |
|  | Jaclang |  |  |  |  |  |

### Hard Problems

| Problem Name | Methodology | Time Taken | Readability | Number of Lines | Token Usage | 
| ------------ | ----------- | ---------- | ----------- | --------------- | ----------- |
| Essay Reviewer | DSpy |  |  |  |  |  |
| | LMQL |  |  |  |  |  |
|  | Jaclang |  |  |  |  |  |
| Wikipedia (ReACT) | DSpy |  |  |  |  |  |
|  | LMQL |  |  |  |  |  |
|  | Jaclang |  |  |  |  |  |