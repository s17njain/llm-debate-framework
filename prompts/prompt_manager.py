# prompts/prompt_manager.py

from config import SCENARIO

def get_base_prompt(role):
    base_prompt = ""
    if (role == "JUDGE"):
        base_prompt += (
            f"You are an impartial ethics evaluator.\n"
            f"Your task is to evaluate the following debate between multiple participants.\n"
            f"Be fair and concise in your evaluation. Do not invent facts. Focus on argument structure, ethical coherence, and clarity of reasoning.\n\n"
            f"Please provide the following in your response:\n"
            f"1. Strengths and weaknesses in each of the participant's argument.\n"
            f"2. Whether any participant showed change in stance and/or showed bias.\n"
            f"3. A score (out of 10) for each participant based on argument structure, ethical coherence, and clarity of reasoning.\n"
            f"4. Which position do you find most convincing, and why.\n\n"
            f"Limit your response to 600 words.\n\n"
        )
    else:
        base_prompt += (
            f"You are an ethics advisor adhering to the principles of {role}.\n"
            f"Your task is to participate in an ongoing policy debate.\n\n"
            f"Scenario:\n{SCENARIO['description']}\n\n"
            f"Limit each of your responses to 300 words.\n\n"
        )
    return base_prompt
