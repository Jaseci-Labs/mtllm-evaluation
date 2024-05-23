import lmql


@lmql.query
def odd_word_out(OPTIONS): # FIXME
    '''lmql
   
    "Pick the odd word out: skirt, dress, pen, jacket.\n"
    "skirt is clothing, dress is clothing, pen is an object, jacket is clothing.\n"
    "So the odd one is pen.\n\n"
    "Pick the odd word out: Spain, France, German, England, Singapore.\n"
    "Spain is a country, France is a country, German is a language, ...\n"
    "So the odd one is German.\n\n"
    "Pick the odd word out: {OPTIONS}\n"
    "[REASONING]"
    "[RESULT]" 
    # where \
    #     not "\n" in REASONING and not "Pick" in REASONING
    return REASONING,RESULT 
    '''

print(odd_word_out('Bentley, Ferrari,Lamborghini, Casio, Toyota'))

'''
argmax
    "Pick the odd word out: skirt, dress, pen, jacket.\n"
    "skirt is clothing, dress is clothing, pen is an object, jacket is clothing.\n"
    "So the odd one is pen.\n\n"
    "Pick the odd word out: Spain, France, German, England, Singapore.\n"
    "Spain is a country, France is a country, German is a language, ...\n"
    "So the odd one is German.\n\n"
    "Pick the odd word out: {OPTIONS}\n"
    "[REASONING]"
    "[RESULT]"
where
    not "\n" in REASONING and not "Pick" in REASONING and
    stops_at(REASONING, "Pick the odd word") and stops_at(REASONING, "\n") and
    stops_at(REASONING, "So the odd one") and stops_at(REASONING, ".") and len(WORDS(REASONING)) < 40
distribute
    RESULT over OPTIONS.split(", ")
'''