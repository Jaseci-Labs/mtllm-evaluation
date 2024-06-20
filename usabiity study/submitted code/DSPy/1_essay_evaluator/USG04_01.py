from pydantic import BaseModel, Field
from typing import List
import dspy

# Define the input model
class Input(BaseModel):
    essay: str = Field(description="The essay to be reviewed")
    criteria: List[str] = Field(description="The criteria for evaluation such as clarity, coherency, etc.")

# Define the output model
class Output(BaseModel):
    remarks: str = Field(description="The evaluator's remarks for the essay")
    grade: str = Field(description="The grade for the essay (A, B, C, D, S, F)")

llm = dspy.OpenAI(model="gpt-3.5-turbo")
dspy.settings.configure(lm=llm)

class EssayEvaluation(dspy.Signature):
    essay: str = dspy.InputField(description="The essay to be reviewed")
    criteria: List[str] = dspy.InputField(description="The criteria for evaluation; clarity and coherency")
    
    remarks: str = dspy.OutputField(description="The evaluator's remarks for the essay")
    grade: str = dspy.OutputField(description="The grade for the essay (A, B, C, D, S, F)")


def evaluate_essay(essay: str, criteria: List[str]) -> Output:
    Response = dspy.Predict(evaluate_essay)(
            essay=essay, criteria=criteria).Response
    
    return Output(remarks=Response.remarks, grade=Response.grade)

input_data = Input(
    essay="The global power crisis is caused by high energy demand, old infrastructure, and reliance on fossil fuels. This crisis results in blackouts, higher costs for businesses, and problems for healthcare and education. To fix this, we need to use more renewable energy like solar and wind, update infrastructure, and use energy more efficiently. Better governance and regulations can help manage the crisis and attract investments for a stable energy future.",
    criteria=["clarity", "coherency"]
)

output_data = evaluate_essay(input_data.essay, input_data.criteria)
print("Evaluator's Remarks: ", output_data.remarks)
print("Grade: ", output_data.grade)
