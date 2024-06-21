import lmql
import asyncio


@lmql.query
async def evaluate_essay(essay: str, criteria: str):
    """
    lmql
    "Evaluate the following essay according to the given criteria and give a grade from A, B, C, D, S, F along with the reasons for that grade.\n\nEssay: {essay}\n\nCriteria: {criteria}"
    """


if __name__ == "__main__":
    essay = input("Enter the essay to be evaluated: ")
    criteria = input("Enter the main criteria for the evaluation: ")

    async def main():
        result = await evaluate_essay(essay, criteria)
        print(f"Grading for the essay: \n{result}")

    asyncio.run(main())
