import lmql
@lmql.query
def essay_remark(essay,criteria):
    '''lmql
    "Give a remark about this essay : {essay} based on criteria : {criteria} [REMARK]" where STOPS_AT(REMARK,".") and len(TOKENS(REMARK)) > 40    

    # return just the ANSWER to the caller
    return ANSWER
    '''
#FUNCTION TO GET THE REMARK
@lmql.query
def essay_grader(essay,criteria):
    '''lmql
    "Give a grade for this essay : {essay} based on criteria : {criteria} [GRADE]." where GRADE in ["A","B","C","D","S","F"]
    
    

    # return just the ANSWER to the caller
    return REMARK
    ''' 


essay = input("Enter your essay : " )
criteria = input("Enter the criteria : ")

print(essay_remark(essay,criteria))
print(essay_grader(essay,criteria))