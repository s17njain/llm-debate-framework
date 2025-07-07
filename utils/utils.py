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
        "total_tokens": 0,
        "output_tokens_details": {
            "reasoning_tokens": 0
        }
    },
    "DEEPSEEK": {
        "completion_tokens": 0,
        "prompt_tokens": 0,
        "prompt_cache_hit_tokens": 0,
        "total_tokens": 0,
        "reasoning_tokens": 0,
        "completion_tokens_details": {
            "reasoning_tokens": 0
        },
        "prompt_cache_miss_tokens": 0
    },
    "CLAUDE": {
        "cache_creation_input_tokens": 0,
        "cache_read_input_tokens": 0,
        "input_tokens": 0,
        "output_tokens": 0,
    },
    "GEMINI": {
        "cached_content_token_count": 0,
        "candidates_token_count": 0,
        "prompt_token_count": 0,
        "thoughts_token_count": 0,
        "total_token_count": 0,
    }
}

def get_models_to_roles_mapping():
    all_roles_perms = list(itertools.permutations(DEBATE_ROLES))
    random.shuffle(all_roles_perms)
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

def write_to_json_file(output_file, content):
    try:
        with open(output_file, 'w', encoding = "utf-8") as f:
            json.dump(content, f, ensure_ascii = False, indent = 4)
    except IOError as e:
        print(f"Error writing to file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def safe_int(val):
    try:
        return int(val)
    except (TypeError, ValueError):
        return 0

def to_dict(obj):
    if isinstance(obj, dict):
        return obj
    elif hasattr(obj, "dict") and callable(obj.dict):
        return obj.dict()
    elif hasattr(obj, "__dict__"):
        return vars(obj)
    else:
        return obj

def update_tokens_usage(current_token_usage, new_token_usage):
    new_token_usage = to_dict(new_token_usage)
    for key, value in new_token_usage.items():
        if key not in current_token_usage:
            continue

        val = to_dict(value)

        if isinstance(val, dict):
            if not isinstance(current_token_usage.get(key), dict):
                current_token_usage[key] = {}
            update_tokens_usage(current_token_usage[key], val)
        else:
            current_token_usage[key] = safe_int(current_token_usage.get(key, 0)) + safe_int(val)
    return current_token_usage
