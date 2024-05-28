## MTLLM (using Anthropic - Claude3 Sonnet)
### Overall Output
```yaml
fromage
```
```yaml
Time Taken: 0.9716598987579346 seconds
```

## LMQL (using OpenAI)
### Overall Output
```yaml
Fromage
```

```yaml
Time Taken: 1.3831193447113037 seconds
```

## DSpy (using OpenAI)
### Overall Output
```yaml
English Word: cheese
Translation: English Word: cheese Translation: fromage
```

```yaml
Time Taken: 3.390303134918213 seconds
```

## Observations
1. MTLLM, LMQL provided the correct translation of the word.
2. DSpy provided the correct translation of the word but also added some unwanted words such as 'English Word:', 'Translation:'.
