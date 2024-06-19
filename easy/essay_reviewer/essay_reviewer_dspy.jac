import:py dspy ;

with entry {
    llm = dspy.OpenAI(model="gpt-4o");    
    dspy.settings.configure(lm=llm) ;
}

class Essay {
    can init(essay: str) {
        self.essay = essay;
    }
    
    can essay_judge(criteria: str) -> str {
        """Evaluate the given essay based on the given criteria. Provide Detailed Judgement."""
        class EssayJudge : dspy.Signature : {
            with entry {
                essay: str = dspy.InputField(desc="Essay");    
                criteria: str = dspy.InputField(desc="Criteria");    
                judgement: str = dspy.OutputField(desc="Judgement");
            }
        }
        
        judgment = dspy.Predict(EssayJudge)(
            essay=self.essay,
            criteria=criteria
        ).judgement;    
        return judgment ;
    }
    
    can generate_summary(judgements: dict) -> str {
        """Generate a summary with the given judgements."""
        class GenerateSummary : dspy.Signature : {
            with entry {
                essay: str = dspy.InputField(desc="Essay");    
                judgements: str = dspy.InputField(desc="Judgements");    
                summary: str = dspy.OutputField(desc="Summary");
            }
        }
        
        summary = dspy.Predict(GenerateSummary)(
            essay=self.essay,
            judgements=str(judgements)
        ).summary;    
        return summary ;
    }
    
    can give_grade(summary: str) -> str {
        """Give essay a letter grade (A-D)."""
        class GiveGrade : dspy.Signature : {
            with entry {
                summary: str = dspy.InputField(desc="Summary");    
                grade: str = dspy.OutputField(desc="Grade");
            }
        }
        
        grade = dspy.Predict(GiveGrade)(summary=summary).grade;    
        return grade ;
    }
}

with entry {
    essay = "With a population of approximately 45 million Spaniards and 3.5 million immigrants,\n        Spain is a country of contrasts where the richness of its culture blends it up with\n        the variety of languages and dialects used. Being one of the largest economies worldwide,\n        and the second largest country in Europe, Spain is a very appealing destination for tourists\n        as well as for immigrants from around the globe. Almost all Spaniards are used to speaking at\n        least two different languages, but protecting and preserving that right has not been\n        easy for them.Spaniards have had to struggle with war, ignorance, criticism and the governments,\n        in order to preserve and defend what identifies them, and deal with the consequences.";    
    essay = Essay(essay);    
    criterias = ["Clarity", "Originality", "Evidence"];    
    judgements = {};    
    for criteria in criterias {
        judgement = essay.essay_judge(criteria);    
        judgements[criteria] = judgement;
    }
    
    summary = essay.generate_summary(judgements);    
    grade = essay.give_grade(summary);    
    print("Reviewer Notes: ", summary) ;    
    print("Grade: ", grade) ;
}

