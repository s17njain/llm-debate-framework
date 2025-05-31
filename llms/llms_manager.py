from openai import OpenAI
import anthropic
from google import genai
from google.genai import types
from config import API_KEYS, MODELS, SYSTEM_ROLE_CONTENT

def get_response_from_llm(model, prompt):
        if (model == "GPT"):
            return get_response_from_gpt(model, prompt)
        elif (model == "DEEPSEEK"):
            return get_response_from_deepseek()
        elif (model == "CLAUDE"):
            return get_response_from_claude()
        elif (model == "GEMINI"):
            return get_response_from_gemini()
        else:
            return ""

def get_response_from_gpt(model, prompt, system_role_content = SYSTEM_ROLE_CONTENT):
    client = OpenAI(
        api_key = API_KEYS.get(model)
    )
    try:
        response = client.responses.create(
            model = MODELS.get(model),
            input = [
                {"role": "developer", "content": system_role_content},
                {"role": "user", "content": prompt}
            ]
        )
        return response.output_text
    except Exception as e:
        print(f"Error extracting response from {model}: {e}")
        return {}

def get_response_from_deepseek(model, prompt, system_role_content = SYSTEM_ROLE_CONTENT):
    client = OpenAI(
        api_key = API_KEYS.get(model),
        base_url="https://api.deepseek.com/v1"
    )
    try:
        response = client.chat.completions.create(
            model = MODELS.get(model),
            messages = [
                {"role": "system", "content": system_role_content},
                {"role": "user", "content": prompt}
            ],
            stream = False
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error extracting response from {model}: {e}")
        return {}

def get_response_from_claude(model, prompt, system_role_content = SYSTEM_ROLE_CONTENT):
    client = anthropic.Anthropic(
        api_key = API_KEYS.get(model)
    )
    try:
        response = client.messages.create(
            model = MODELS.get(model),
            system = system_role_content,
            messages = [
                {"role": "user", "content": prompt}
            ]
        )
        return response.content
    except Exception as e:
        print(f"Error extracting response from {model}: {e}")
        return {}

def get_response_from_gemini(model, prompt, system_role_content = SYSTEM_ROLE_CONTENT):
    client = genai.Client(
        api_key = API_KEYS.get(model)
    )
    try:
        response = client.models.generate_content(
            model = MODELS.get(model),
            config = types.GenerateContentConfig(
                system_instruction = system_role_content),
            contents = prompt
        )
        return response.text
    except Exception as e:
        print(f"Error extracting response from {model}: {e}")
        return {}

