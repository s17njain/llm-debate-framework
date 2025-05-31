import os
import uuid
from config import SCENARIO, OUTPUT_DIR, TURN_LIMIT
from utils.utils import get_models_to_roles_mapping
from prompts.prompt_manager import get_base_prompt
from llms.llms_manager import get_response_from_llm

def run_debate_sessions():
    os.makedirs(OUTPUT_DIR, exist_ok = True)

    models_to_roles_mappings = get_models_to_roles_mapping()

    for i, mapping in enumerate(models_to_roles_mappings):
        session_id = f"session_{i+1}_{uuid.uuid4().hex[:6]}"
        print(f"\nStarting Debate Session: {session_id}")

        # judge_model = [model for model, role in mapping.items() if role == "JUDGE"][0]
        debate_assignments = {model: role for model, role in mapping.items() if role != "JUDGE"}

        transcript_path = os.path.join(OUTPUT_DIR, f"{session_id}_transcript.txt")
        run_single_debate(session_id, debate_assignments, transcript_path)

        # # pass transcript to judge
        # transcript_path = os.path.join(OUTPUT_DIR, f"{session_id}_transcript.txt")
        # run_judging(transcript_path=transcript_path, judge_model=judge_model, session_id=session_id)

        print(f"\nDebate Session {session_id} concluded.\n")


def run_single_debate(session_id, debate_assignments, transcript_path):
    with open(transcript_path, "w") as f:
        f.write(f"### Debate Session: {session_id}\n\n")
        f.write(f"## Scenario:\n{SCENARIO.get('description')}\n\n")
        f.write("## Role Assignments:\n")
        for model, role in debate_assignments.items():
            f.write(f"{model}: {role}\n")
        f.write("\n\n")

    model_history = {}
    prev_responses = []

    for turn in range(TURN_LIMIT):
        print(f"\nTurn {turn + 1}")

        with open(transcript_path, "a") as f:
            f.write(f"## Turn {turn + 1}\n\n")

        for index, (model, role) in enumerate(debate_assignments.items()):
            current_model_history = ""

            if (model in model_history):
                current_model_history += model_history.get(model)
            else:
                prompt = get_base_prompt(role)
                current_model_history += prompt

            if (len(prev_responses) > 2):
                prev_responses.pop(0)

            for prev_resp in prev_responses:
                current_model_history += prev_resp

            print(f"{model} ({role}) responding...")
            # response = get_response_from_llm(model, current_model_history)
            response = f"Hello from {model}"

            current_model_history += f"You ({role}):\n{response.strip()}\n\n"
            model_history[model] = current_model_history
            prev_responses.append(f"{model} ({role}):\n{response.strip()}\n\n")

            with open(transcript_path, "a") as f:
                f.write(f"{model} ({role}):\n{response.strip()}\n\n")
