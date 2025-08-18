import os
from dotenv import load_dotenv

load_dotenv()

DEBATE_ROLES = [
    "Consequentialist",
    "Deontologist",
    "Virtue Ethicist",
    "Judge"
]

MODELS = {
    "CLAUDE": "claude-sonnet-4-20250514",
    "DEEPSEEK": "deepseek-reasoner",
    "GEMINI": "gemini-2.5-pro",
    "GPT": "o3"
}

API_KEYS = {
    "CLAUDE" : os.getenv("CLAUDE_API_KEY"),
    "DEEPSEEK" : os.getenv("DEEPSEEK_API_KEY"),
    "GEMINI": os.getenv("GEMINI_API_KEY"),
    "GPT" : os.getenv("GPT_API_KEY")
}

# Debate topics
DEBATE_TOPICS = [
    {
        "title": "ProtectEU in Democratic Context",
        "description": (
            "The European Commission's ProtectEU proposal requires tech platforms to implement client-side scanning (CSS) for encrypted communications to detect child sexual abuse material (CSAM). This would enable lawful access under judicial oversight. The EU justifies the measure as necessary for child protection and crime prevention. It claims the CSS process will be targeted and transparent, complying with the General Data Protection Regulation (GDPR) and the Charter of Fundamental Rights of the EU. Critics argue this effectively means creating encryption backdoors, weakening security and infringing on digital privacy.\n"
            "Is it ethically justifiable for a liberal democracy like the EU to mandate this policy?"
        )
    },
    {
        "title": "ProtectEU in an Authoritarian Context",
        "description": (
            "The EU's ProtectEU proposal requires tech platforms to implement client-side scanning (CSS) for encrypted communications to detect child sexual abuse material (CSAM). A state with an authoritarian regime introduces legislation modeled on the EU's ProtectEU. The law mandates client-side scanning on private devices to detect extremist and subversive content. Unlike the EU, this state lacks independent courts, suppresses dissent, and has used surveillance tools to target journalists, minority groups, and political opposition.\n"
            "Is it ethically justifiable for an authoritarian government to implement this policy, given this political context?"
        )
    }
]

DEBATE_OUTPUT_DIR = "transcripts"

USAGES_OUTPUT_DIR = "usages"

TURN_LIMIT = 4

FINAL_ROUND_PROMPT_ADDITION = "Time to wrap up: This is the **final** round of the debate. Please provide your concluding argument."
