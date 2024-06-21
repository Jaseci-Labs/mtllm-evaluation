import torch
from transformers import LlamaForCausalLM, LlamaTokenizer


class EssayEvaluator:
    def __init__(self, model_name="llama2"):
        self.tokenizer = LlamaTokenizer.from_pretrained(model_name)
        self.model = LlamaForCausalLM.from_pretrained(model_name)

    def evaluate_essay(self, essay, criteria):
        criteria_str = ", ".join(criteria)
        prompt = f"""
        Evaluate the following essay based on the criteria provided:

        Essay: {essay}

        Criteria for evaluation: {criteria_str}

        Please provide detailed evaluator remarks for the essay based on the given criteria and assign a grade (A, B, C, D, S, F).

        Evaluator's Remarks:
        """

        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(inputs.input_ids, max_length=300, temperature=0.7)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Extract remarks and grade
        remarks_start = response.find("Evaluator's Remarks:") + len(
            "Evaluator's Remarks:"
        )
        remarks = response[remarks_start:].strip()
        grade = (
            remarks.split()[-1]
            if remarks.split()[-1] in ["A", "B", "C", "D", "S", "F"]
            else "N/A"
        )

        return remarks, grade


if __name__ == "__main__":
    essay = "The global power crisis is caused by high energy demand, old infrastructure, and reliance on fossil fuels. This crisis results in blackouts, higher costs for businesses, and problems for healthcare and education. To fix this, we need to use more renewable energy like solar and wind, update infrastructure, and use energy more efficiently. Better governance and regulations can help manage the crisis and attract investments for a stable energy future."
    criteria = ["clarity", "coherence", "grammar", "relevance", "structure"]

    evaluator = EssayEvaluator(model_name="llama2")
    remarks, grade = evaluator.evaluate_essay(essay, criteria)

    print("Evaluator's Remarks:\n", remarks)
    print("\nGrade:", grade)
