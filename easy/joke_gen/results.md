## MTLLM (using Anthropic - Claude3 Sonnet)
### Overall Output
```yaml
What do you call a fake noodle? : An Impasta.
```
```yaml
Time taken: 2.452475070953369 seconds
```

## LMQL (using OpenAI)
### Overall Output
```yaml
Why couldn't the bicycle stand up by itself? :  Because it was two-tired.
```

```yaml
Time taken: 5.55 seconds
```

## DSpy (using OpenAI)
### Overall Output
```yaml
raise ValueError(
ValueError: ('Too many retries trying to get the correct output format. Try simplifying the requirements.', {'general': 'Field required: joke (error type: missing); Field required: punchline (error type: missing)'})
```

## Observations
1. MTLLM & LMQL provided accurate answers.
2. DSpy failed to provide an answer. Code needs to be modified to handle such cases. Wasnt abled to figure out the issue.