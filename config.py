import os
from dotenv import load_dotenv

load_dotenv()

DEBATE_ROLES = {
    "CONSEQUENTIALIST": "Consequentialist",
    "DEONTOLOGIST": "Deontologist",
    "VIRTUE_ETHICIST": "Virtue Ethicist",
    "JUDGE": "Judge"
}

MODELS = {
    "GPT": "gpt-4.1",
    "DEEPSEEK": "deepseek-reasoner",
    "CLAUDE": "claude-3-7-sonnet-latest",
    "GEMINI": "gemini-2.5-pro-preview-05-06"
}

API_KEYS = {
    "GPT" : os.getenv("GPT_API_KEY"),
    "DEEPSEEK" : os.getenv("DEEPSEEK_API_KEY"),
    "CLAUDE" : os.getenv("CLAUDE_API_KEY"),
    "GEMINI": os.getenv("GEMINI_API_KEY")
}

SCENARIO = {
    "title": "ProtectEU Encryption Backdoor Debate",
    "description": (
        "The ProtectEU initiative, backed by the European Commission, proposes mechanisms for lawful access to encrypted data to combat serious crimes like terrorism and child exploitation. Critics argue this effectively means creating backdoors in end-to-end encryption, weakening security and infringing on digital privacy. Supporters argue this is essential for public safety and democratic accountability.\n"
        "Should the government mandate encryption backdoors under the ProtectEU initiative?"
    )
}

OUTPUT_DIR = "transcripts"

TURN_LIMIT = 3   # For now; can be adjusted

SYSTEM_ROLE_CONTENT = "You are an ethics advisor."

JUDGE_ROLE_CONTENT = "You are an impartial ethics evaluator."
