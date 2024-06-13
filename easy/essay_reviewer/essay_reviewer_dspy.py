import dspy

llm = dspy.OpenAI(model="gpt-4o")
dspy.settings.configure(lm=llm)


class Essay:
    def __init__(self, essay: str):
        self.essay = essay

    def essay_judge(self, criteria: str) -> str:
        class EssayJudge(dspy.Signature):
            """Evaluate the given essay based on the given criteria. Provide Detailed Judgement."""

            essay: str = dspy.InputField(desc="Essay")
            criteria: str = dspy.InputField(desc="Criteria")
            judgement: str = dspy.OutputField(desc="Judgement")

        judgment = dspy.Predict(EssayJudge)(
            essay=self.essay, criteria=criteria
        ).judgement
        return judgment

    def generate_summary(self, judgements: dict) -> str:
        class GenerateSummary(dspy.Signature):
            """Generate a summary with the given judgements."""

            essay: str = dspy.InputField(desc="Essay")
            judgements: str = dspy.InputField(desc="Judgements")
            summary: str = dspy.OutputField(desc="Summary")

        summary = dspy.Predict(GenerateSummary)(
            essay=self.essay, judgements=str(judgements)
        ).summary
        return summary

    def give_grade(self, summary: str) -> str:
        class GiveGrade(dspy.Signature):
            """Give essay a letter grade (A-D)."""

            summary: str = dspy.InputField(desc="Summary")
            grade: str = dspy.OutputField(desc="Grade")

        grade = dspy.Predict(GiveGrade)(summary=summary).grade
        return grade


essay = "Sigiriya is an ancient rock fortress located in central Sri Lanka. Rising up 660 feet (200 meters) from the surrounding plains, the massive rock column was transformed into an impregnable palace-fortress in the late 5th century AD by King Kasyapa. The site contains the ruins of elaborate gardens, fountains, frescoes of maidens that once adorned the rock face, and a gateway in the form of an enormous lion. Declared a UNESCO World Heritage Site in 1982, Sigiriya is considered one of the best preserved examples of ancient urban planning and is one of Sri Lanka's major attractions for visitors due to its archaeological significance and striking aesthetic beauty."

essay = Essay(essay)
criterias = ["Clarity", "Originality", "Evidence"]
judgements = {}
for criteria in criterias:
    judgement = essay.essay_judge(criteria)
    judgements[criteria] = judgement
summary = essay.generate_summary(judgements)
grade = essay.give_grade(summary)
print("Reviewer Notes: ", summary)
print("Grade: ", grade)
