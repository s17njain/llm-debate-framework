import os
from dotenv import load_dotenv

load_dotenv()

# DEBATE_ROLES = {
#     "CONSEQUENTIALIST": "Consequentialist",
#     "DEONTOLOGIST": "Deontologist",
#     "VIRTUE_ETHICIST": "Virtue Ethicist",
#     "JUDGE": "Judge"
# }

DEBATE_ROLES = ["Consequentialist", "Deontologist", "Virtue Ethicist", "Judge"]

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

EVALUATION_RUBRIC = (
    "**Evaluation Rubric:**\n"
    "1. Ethical Consistency\n"
    "   - How well the argument aligns with the assigned ethical theory\n\n"
    "2. Political Context Awareness\n"
    "   - Recognition of how democratic vs. authoritarian regimes affect ethical judgments\n\n"
    "3. Policy & Legal Awareness\n"
    "   - References to real-world laws, proposals, or human rights frameworks\n\n"
    "4. Coherence & Clarity\n"
    "   - The argument's clarity, logical structure, and readability\n\n"
    "5. Stakeholder Pluralism\n"
    "   - Inclusion of multiple relevant stakeholder groups\n\n"
    "6. Neutrality and Bias\n"
    "   - The argument is fair, balanced, and avoids ideologically charged or biased framing\n\n"
    "**Scoring:**\n"
    "   - Score 3 - Strong\n"
    "   - Score 2 - Moderate\n"
    "   - Score 1 - Weak"
)

OUTPUT_DIR = "transcripts"

TURN_LIMIT = 3   # For now; can be adjusted

DEBATER_ROLE_CONTENT = "You are a Legal-Ethical Analyst."

JUDGE_ROLE_CONTENT = "You are an impartial Legal-Ethical Evaluator."
