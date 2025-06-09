from config import EVALUATION_RUBRIC

def get_base_prompt(role, debate_topic = None):
    if (role == "Judge"):
        return (
            f"You are an impartial **Legal-Ethical Evaluator**, acting in the role of a **{role}**.\n"
            f"Your task is to evaluate the following debate between multiple participants.\n"
            f"Please evaluate the debate based on the evaluation rubric as defined below.\n\n"
            f"{EVALUATION_RUBRIC}\n\n"
            f"Please justify each part of your evaluation. Be fair and concise in your evaluation. Do not invent facts.\n"
            f"In the end, please answer: Which position do you find most convincing, and why?\n"
            f"Limit your response to 1000 words.\n\n"
        )
    else:
        return (
            # f"You are an ethics advisor adhering to the principles of **{role}**.\n"
            f"You are a **Legal-Ethical Analyst** adhering to the principles of **{role}**.\n"
            f"Your task is to participate in an ongoing policy debate.\n\n"
            f"**Debate Topic:**\n{debate_topic.get('description')}\n\n"
            f"Limit each of your responses to 300 words.\n\n"
        )
