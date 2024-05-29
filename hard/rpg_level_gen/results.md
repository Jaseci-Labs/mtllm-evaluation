## MTLLM  without Rules
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

## LMQL 
### Overall Output
```yaml

```

```yaml

```

## DSpy 
### Error Encountered
```bash
Traceback (most recent call last):
  File "/workspaces/mtllm-evaluation/hard/rpg_level_gen/level_dspy.py", line 116, in <module>
    level_manager.get_next_level()
  File "/workspaces/mtllm-evaluation/hard/rpg_level_gen/level_dspy.py", line 78, in get_next_level
    new_level_map = dspy.TypedPredictor(CreateMap)(level=new_level).map
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/mtllm_eval/lib/python3.12/site-packages/dspy/primitives/program.py", line 26, in __call__
    return self.forward(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/envs/mtllm_eval/lib/python3.12/site-packages/dspy/functional/functional.py", line 235, in forward
    raise ValueError(
ValueError: ('Too many retries trying to get the correct output format. Try simplifying the requirements.', {'map': "ValueError('json output should end with ```')"})
```
This error was encountered because of max_tokens limit.
After increasing the max_tokens limit, the output was generated.

### Overall Output
```yaml
name="Novice's Challenge" difficulty=1 width=12 height=12 num_wall=6 num_enemies=3 time_countdown=280 n_retries_allowed=5
BBBBBBBBBBBBBB
BP...........B
B.B....B.....B
B..B...B...B.B
B..BB..B...B.B
B..B.BBBB..B.B
B..B..B....B.B
B....E...B...B
B.......BB...B
B...BBBE.B...B
B........BB..B
B........E...B
B............B
BBBBBBBBBBBBBB
name='Advanced Trial' difficulty=2 width=16 height=16 num_wall=10 num_enemies=5 time_countdown=240 n_retries_allowed=4
BBBBBBBBBBBBBBBBBB
B................B
B.P..B.........B.B
B..B.B.....B...B.B
B..BBB.B...B...B.B
B..B.B.B...B.B.B.B
B..B..BB.B.B.B.B.B
B....E.B.B.B.B...B
B......BBB...B...B
B......E.B...B...B
B........BB......B
B...BBBBBE.......B
B...........B....B
B.....BBBBBE.....B
B................B
B...........BEBBBB
B................B
BBBBBBBBBBBBBBBBBB
```
```yaml
Time Taken: 51.75 seconds
```

## Observations
1. MTLLM is able to generate levels with the given constraints and the output is as expected and Ability to create Nested Objects with Precision.
2. DSpy is able to generate levels with the given constraints and the output is as expected and Ability to create Nested Objects with Precision.