## MTLLM (using Anthropic - Claude3 Sonnet) without Rules
### Overall Output
```yamlLevel(name='Level 2', difficulty=1, width=12, height=12, num_wall=6, num_enemies=4, time_countdown=150, n_retries_allowed=3)
BBBBBBBBBBBBBB
B............B
B.B..........B
B..E.....B...B
B..BBBB..B..EB
B........B...B
B.....E..B...B
B.......BBB..B
B....BBBB....B
B........E...B
B...BBBB.....B
B..........B.B
B.P........BBB
BBBBBBBBBBBBBB

Level(name='Level 4', difficulty=2, width=16, height=16, num_wall=10, num_enemies=8, time_countdown=210, n_retries_allowed=2)
BBBBBBBBBBBBBBBBBB
B................B
B.P......E.......B
B.......B.....B..B
B..BBBBB......B..B
B...E.........B..B
B.........BBBBB..B
B.B.........E....B
B.B..BBBB....BE..B
B.B....E.........B
B.B........BBBBB.B
B...............BB
B..BBBB........EBB
B.....B.........BB
B..E.....BBBB...BB
B...BBBB...E.....B
B.........B......B
BBBBBBBBBBBBBBBBBB
```
```yaml
Time Taken: 31.99008297920227 seconds
```

## MTLLM (using Anthropic - Claude3 Sonnet) with Rules
### Overall Output
```yaml

```

```yaml

```

## LMQL (using OpenAI)
### Overall Output
```yaml

```

```yaml

```

## DSpy (using OpenAI)
### Error Encountered
```bash
raise ValueError(
ValueError: ('Too many retries trying to get the correct output format. Try simplifying the requirements.', {'general': 'Field required: translation (error type: missing)'})
```

## Observations
1. MTLLM is able to generate levels with the given constraints and the output is as expected and Ability to create Nested Objects with Precision.