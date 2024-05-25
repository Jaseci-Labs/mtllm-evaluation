import lmql


@lmql.query()
def translate(english_word):
    '''lmql
    """
        "sea otter": "loutre de mer",
        "peppermint": "menthe poivrée",
        "plush giraffe": "girafe en peluche"
    """
    "Q: What is the translation of {english_word}?\n"
    "A:[ANSWER]"
    return f'{ANSWER}'
    '''


print(translate("cheese"))
