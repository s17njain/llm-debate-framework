import itertools
import random
import json
from config import DEBATE_ROLES, MODELS

INITIAL_USAGES = {
    "GPT": {
        "input_tokens": 0,
        "cached_tokens": 0,
        "output_tokens": 0,
        "reasoning_tokens": 0,
        "total_tokens": 0
    },
    "DEEPSEEK": {
        "completion_tokens": 0,
        "prompt_tokens": 0,
        "prompt_cache_hit_tokens": 0,
        "prompt_cache_miss_token": 0,
        "total_tokens": 0,
        "reasoning_tokens": 0
    },
    "CLAUDE": {
        "cache_creation_input_tokens": 0,
        "cache_read_input_tokens": 0,
        "input_tokens": 0,
        "output_tokens": 0
    },
    "GEMINI": {
        "cached_content_token_count": 0,
        "candidates_token_count": 0,
        "prompt_token_count": 0,
        "thoughts_token_count": 0,
        "total_token_count": 0
    }
}

def get_models_to_roles_mapping():
    all_roles_perms = list(itertools.permutations(DEBATE_ROLES))
    models = list(MODELS.keys())
    random.shuffle(models)
    unique_mappings = []

    used_by_key = {k: set() for k in models}

    for roles_perm in all_roles_perms:
        candidate = dict(zip(models, roles_perm))

        conflict = False
        for k, v in candidate.items():
            if v in used_by_key[k]:
                conflict = True
                break

        if not conflict:
            unique_mappings.append(candidate)
            for k, v in candidate.items():
                used_by_key[k].add(v)

        if all(len(v) == len(models) for v in used_by_key.values()):
            break

    return unique_mappings

def update_tokens_usage(model, current_token_usage, new_token_usage):
    if (model == "GPT"):
        return _update_gpt_usage(current_token_usage, new_token_usage)
    elif (model == "DEEPSEEK"):
        return _update_deepseek_usage(current_token_usage, new_token_usage)
    elif (model == "CLAUDE"):
        return _update_claude_usage(current_token_usage, new_token_usage)
    elif (model == "GEMINI"):
        return _update_gemini_usage(current_token_usage, new_token_usage)
    else:
        return ""


def _update_gpt_usage(current_token_usage, new_token_usage):
    if new_token_usage:
        new_token_usage_dict = new_token_usage.dict()
        current_token_usage["input_tokens"] += new_token_usage_dict.get("input_tokens") or 0
        current_token_usage["cached_tokens"] += new_token_usage_dict.get("input_tokens_details", {}).get("cached_tokens") or 0
        current_token_usage["output_tokens"] += new_token_usage_dict.get("output_tokens") or 0
        current_token_usage["reasoning_tokens"] += new_token_usage_dict.get("output_tokens_details", {}).get("reasoning_tokens") or 0
        current_token_usage["total_tokens"] += new_token_usage_dict.get("total_tokens") or 0
    return current_token_usage

def _update_deepseek_usage(current_token_usage, new_token_usage):
    if new_token_usage:
        new_token_usage_dict = new_token_usage.dict()
        current_token_usage["completion_tokens"] += new_token_usage_dict.get("completion_tokens") or 0
        current_token_usage["prompt_tokens"] += new_token_usage_dict.get("prompt_tokens") or 0
        current_token_usage["prompt_cache_hit_tokens"] += new_token_usage_dict.get("prompt_cache_hit_tokens") or 0
        current_token_usage["prompt_cache_miss_token"] += new_token_usage_dict.get("prompt_cache_miss_token") or 0
        current_token_usage["total_tokens"] += new_token_usage_dict.get("total_tokens") or 0
        current_token_usage["reasoning_tokens"] += new_token_usage_dict.get("completion_tokens_details", {}).get("reasoning_tokens") or 0
    return current_token_usage

def _update_claude_usage(current_token_usage, new_token_usage):
    if new_token_usage:
        new_token_usage_dict = new_token_usage.dict()
        current_token_usage["cache_creation_input_tokens"] += new_token_usage_dict.get("cache_creation_input_tokens") or 0
        current_token_usage["cache_read_input_tokens"] += new_token_usage_dict.get("cache_read_input_tokens") or 0
        current_token_usage["input_tokens"] += new_token_usage_dict.get("input_tokens") or 0
        current_token_usage["output_tokens"] += new_token_usage_dict.get("output_tokens") or 0
    return current_token_usage

def _update_gemini_usage(current_token_usage, new_token_usage):
    if new_token_usage:
        new_token_usage_dict = new_token_usage.dict()
        current_token_usage["cached_content_token_count"] += new_token_usage_dict.get("cached_content_token_count") or 0
        current_token_usage["candidates_token_count"] += new_token_usage_dict.get("candidates_token_count") or 0
        current_token_usage["prompt_token_count"] += new_token_usage_dict.get("prompt_token_count") or 0
        current_token_usage["thoughts_token_count"] += new_token_usage_dict.get("thoughts_token_count") or 0
        current_token_usage["total_token_count"] += new_token_usage_dict.get("total_token_count") or 0
    return current_token_usage

def write_to_json_file(output_file, content):
    try:
        with open(output_file, 'w', encoding = "utf-8") as f:
            json.dump(content, f, ensure_ascii = False, indent = 4)
    except IOError as e:
        print(f"Error writing to file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
