import:py random;
import:py from jaclang.core.llms, Anthropic;


glob llm = Anthropic(model_name="claude-3-sonnet-20240229");

can 'Evaluate an essay by the criteria given and give a remark about the text without repreating the text also give a grade from A,B,C,D,S,F.' text_evaluater(text:'text':str, criteriaToEvaluate:'Criteria to evaluate':str)->'remark for the text based on the criteria and grade from A,B,C,D,S,F' : str by llm();


obj Output{
    has description:'everything except the grade':str,
        grade:str;
}
with entry{
    cont:str = "y";
    while(cont == "y"){
        print("----------------WELCOME.!----------------");
        text:str = input("Hi give an input : ");
        criteria:str = input("Which criteria do you want to check ? ");
        checker:str=text_evaluater(text,criteria);
        essayObj = Output(by llm(incl_info = (checker)));

        
        print(essayObj.description);
        print(essayObj.grade);
        cont = input("Continue? (y/n) ");
    }
        
    
}