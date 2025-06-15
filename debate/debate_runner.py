import os
import uuid
import random
from config import DEBATE_TOPICS, OUTPUT_DIR, TURN_LIMIT
from utils.utils import get_models_to_roles_mapping
from prompts.prompt_manager import get_base_prompt
from llms.llms_manager import get_response_from_llm
from judge.judge_manager import run_judging

def run_debate_sessions(shuffle_speakers = False):
    os.makedirs(OUTPUT_DIR, exist_ok = True)

    models_to_roles_mappings = get_models_to_roles_mapping()

    for i, debate_topic in enumerate(DEBATE_TOPICS):
        for j, mapping in enumerate(models_to_roles_mappings):
            session_id = f"debate_{i+1}_session_{j+1}_{uuid.uuid4().hex[:6]}"
            print("--------------------------------------------------------------------------------")
            print(f"Starting Debate Session: **{session_id}**\n")

            judge_assignment = {model: role for model, role in mapping.items() if role == "Judge"}
            debate_assignments = {model: role for model, role in mapping.items() if role != "Judge"}

            transcript_path = os.path.join(OUTPUT_DIR, f"{session_id}_transcript.txt")

            # run current debate session
            _run_single_debate(session_id, debate_assignments, debate_topic, transcript_path, shuffle_speakers)

            # pass transcript to judge
            run_judging(transcript_path, judge_assignment)

            print(f"\nDebate session concluded.")
            print(f"Debate transcript saved to: {transcript_path}")
            print("--------------------------------------------------------------------------------\n")

def _run_single_debate(session_id, debate_assignments, debate_topic, transcript_path, shuffle_speakers):
    with open(transcript_path, "w") as f:
        f.write(f"# Debate Session:\n{session_id}\n\n")
        f.write(f"## Debate Topic:\n{debate_topic.get('description')}\n\n")
        f.write("## Debate Role Assignments:\n")
        for model, role in debate_assignments.items():
            f.write(f"{model}: {role}\n")
        f.write("\n")
        f.write("## Debate:\n")

    model_history = {}
    prev_responses = []
    prev_speaker_order = []
    prev_speaker = None

    debate_starter = True
    for _ in range(TURN_LIMIT):
        debate_assignments_items = list(debate_assignments.items())

        # shuffle order of speakers
        if (shuffle_speakers):
            while True:
                random.shuffle(debate_assignments_items)
                keys = [k for k, _ in debate_assignments_items]
                if (not prev_speaker_order or keys != prev_speaker_order) and (prev_speaker is None or keys[0] != prev_speaker):
                    break

        for model, role in debate_assignments_items:
            current_model_history = ""

            if (model in model_history):
                current_model_history += model_history.get(model)
            else:
                prompt = get_base_prompt(role, debate_topic)
                current_model_history += prompt

            if (len(prev_responses) >= len(debate_assignments)):
                prev_responses.pop(0)

            for prev_resp in prev_responses:
                current_model_history += prev_resp

            print(f"{model} ({role}) responding...")
            # response = get_response_from_llm(model, (current_model_history + ("Empty\n\n" if debate_starter else "")))
            debate_starter = False
            response = f"Hello from {model}"

            current_model_history += f"You ({role}):\n{response.strip()}\n\n"
            model_history[model] = current_model_history
            prev_responses.append(f"{model} ({role}):\n{response.strip()}\n\n")

            with open(transcript_path, "a") as f:
                f.write(f"{model} ({role}):\n{response.strip()}\n\n")

        if (shuffle_speakers):
            prev_speaker_order = keys
            prev_speaker = keys[-1]
