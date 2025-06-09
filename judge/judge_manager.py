from prompts.prompt_manager import get_base_prompt
from llms.llms_manager import get_response_from_llm
from config import JUDGE_ROLE_CONTENT

def run_judging(transcript_path, judge_assignment):
    judge_model, judge_role = next(iter(judge_assignment.items()))
    judge_base_prompt = get_base_prompt(judge_role)
    
    debate_transcript = "**Debate Transcript:**\n"
    with open(transcript_path, "r") as f:
        debate_transcript += f.read()
    
    print(f"\n{judge_model} ({judge_role}) evaluating...")
    # judge_response = get_response_from_llm(judge_model, (judge_base_prompt + debate_transcript), JUDGE_ROLE_CONTENT)
    judge_response = f"Hello from {judge_model}"

    with open(transcript_path, "a") as f:
        f.write(f"## Evaluation:\n")
        f.write(f"{judge_model} ({judge_role}):\n{judge_response.strip()}\n")
