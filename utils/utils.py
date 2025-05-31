import itertools
from config import DEBATE_ROLES, MODELS

def get_models_to_roles_mapping():
    all_roles_perms = list(itertools.permutations(DEBATE_ROLES.keys()))
    models = list(MODELS.keys())
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
