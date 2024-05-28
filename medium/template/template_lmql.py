import lmql


@lmql.query
def bruno_mars():  # FIXME
    '''lmql
    """Write a summary of Bruno Mars, the singer:
    {{
        \"name\": \"[STRING_VALUE]\",
        \"age\": [INT_VALUE],
        \"top_songs\": [[\"[STRING_VALUE]\", \"[STRING_VALUE]\"]]
    }}""" where \
        STOPS_BEFORE(STRING_VALUE, '"') and INT(INT_VALUE) and len(TOKENS(INT_VALUE)) < 2
    return STRING_VALUE, INT_VALUE
    '''


print(bruno_mars())
