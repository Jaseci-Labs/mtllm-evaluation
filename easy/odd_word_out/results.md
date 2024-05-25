## MTLLM (using Anthropic - Claude3 Sonnet)
### Overall Output
```yaml
('Casio is a watch company, Bentley, Ferrari, Lamborghini, Toyota are car companies.', 'Casio')
```
```yaml
Time taken: 2.600358009338379  seconds
```

## LMQL (using OpenAI)
### Overall Output
```yaml
('Bentley, Ferrari, and Lamborghini are all luxury car brands, while Casio and Toyota are not. So the odd one out is Casio.', '')
```

```yaml
Time taken: 2.7534639835357666 seconds
```

## DSpy (using OpenAI)

## Erros Encountered
1. When I tried to provide the input to Signature as a list of strings, I got the following error:
```python
import dspy

turbo = dspy.OpenAI(model="gpt-3.5-turbo")
dspy.settings.configure(lm=turbo)

class OddWordOut(dspy.Signature):
    """Pict the Odd Word Out from the given list of words."""

    options: list[str] = dspy.InputField(desc="Options to pick from")
    odd_word: str = dspy.OutputField(desc="Odd Word")

pred = dspy.ChainOfThought(OddWordOut)(options=["Bentley", "Ferrari", "Lamborghini", "Casio", "Toyota"])
print((pred.odd_word, pred.rationale))
``` 
```python
assert type(x) == str, f"Need format_handler for {field.input_variable} of type {type(x)}"
           ^^^^^^^^^^^^^^
AssertionError: Need format_handler for options of type <class 'list'>
```
### Overall Output (Without Examples)
```yaml
('produce the odd word. We can see that the first four options are all luxury car brands, while Toyota is a mainstream car brand.', 'Toyota')
```

```yaml
Time taken: 1.50 seconds
```

### Overall Output (With Examples)
```yaml
('Casio', "produce the odd word. We can see that 'Casio' is the only brand that is not a luxury car brand.")
```

```yaml
Time taken: 3.75 seconds
```

## Observations
1. MTLLM provided the most accurate answer to the question.
2. LMQL was not able to follow the expected format. But was able to provide the correct reasoning. without the correct answer.
3. DSpy was unable to provide the correct answer when examples were not provided. But was able to provide the correct answer when examples were provided. While introducing some unwanted words `produce the odd word.`.
4. DSPy Implementation with Examples (Few Shot Prompting) is hard to implement. Seems like a such an overkill for such a simple problem.