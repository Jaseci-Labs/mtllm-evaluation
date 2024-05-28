## MTLLM 
### Overall Output
```yaml
Question:  Where is Apple Headquaters located?
Answer:  Cupertino, California, United States
Question:  Who is Jason Mars?
Answer:  Jason Mars is an American computer scientist, author, and entrepreneur known for his work in AI and computer architecture.
```
```yaml
Time Taken: 8.737410545349121 seconds
```

## MTLLM (Without using Typed Outputs)

### Overall Output
```yaml
Question:  Where is Apple Headquaters located?
Answer:  Cupertino, California, United States
Question:  Who is Jason Mars?
Answer:  Jason Mars is an American computer scientist, author, and entrepreneur known for his work in computer architecture and artificial intelligence. He is an Associate Professor at the University of Michigan and co-director of U-M's Clarity Lab.
```

```yaml
Time taken:  11.804817199707031 seconds
```

## LMQL 
### Overall Output
```yaml
Not Available
```

```yaml
Not Available
```

## DSpy 
### Overall Output
```yaml
Question:  Where is Apple Headquaters located?
Answer:  Final Answer
---
Final Answer: Apple Headquarters is located in Cupertino, California, United States.
Question:  Who is Jason Mars?
Answer:  Jason Mars is an American computer scientist, author, and entrepreneur known for his work in computer architecture and AI, particularly in conversational AI. He is an Associate Professor at the University of Michigan and has been involved in several AI initiatives and startups.
```

```yaml
Time Taken: 10.763540029525757 seconds
```

## Observations
1. MTLLM provided the most accurate and detailed answers to the questions. while following the expected format.
2. DSpy was able to provide the correct answers but added some unwanted words such as 'Final Answer:', 'Question:'. Showing that it was not able to follow the expected format using the example provided.
