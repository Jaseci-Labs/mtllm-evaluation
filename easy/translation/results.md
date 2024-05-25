## MTLLM (using Anthropic - Claude3 Sonnet)
### Overall Output
```yaml
fromage
```
```yaml
Time taken: 1.8196868896484375  seconds
```

## LMQL (using OpenAI)
### Overall Output
```yaml
 Fromage
```

```yaml
Time taken: 2.45 seconds
```

## DSpy (using OpenAI)
### Overall Output
```yaml
raise ValueError(
ValueError: ('Too many retries trying to get the correct output format. Try simplifying the requirements.', {'general': 'Field required: translation (error type: missing)'})
```

## Observations
1. MTLLM & LMQL provided accurate answers.
2. DSpy failed to provide an answer. Code didnt worked. Same code worked for other examples.