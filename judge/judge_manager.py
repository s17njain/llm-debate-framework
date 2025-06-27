from prompts.prompt_manager import get_base_prompt
from llms.llms_manager import get_response_from_llm

def run_judging(transcript_path, judge_assignment, token_usages):
    judge_model, judge_role = next(iter(judge_assignment.items()))
    judge_base_prompt = get_base_prompt(judge_role)
    
    debate_transcript = "**Debate Transcript:**\n"
    with open(transcript_path, "r", encoding='utf-8') as f:
        debate_transcript += f.read()
    
    print(f"\n{judge_model} ({judge_role}) evaluating...")
    judge_response = get_response_from_llm(judge_model, (judge_base_prompt + debate_transcript), token_usages)

    with open(transcript_path, "a", encoding='utf-8') as f:
        f.write(f"## Evaluation:\n")
        f.write(f"### {judge_model} ({judge_role}):\n{judge_response.strip()}\n")
