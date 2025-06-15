from openai import OpenAI
import anthropic
from google import genai
from config import API_KEYS, MODELS
import sys

def get_response_from_llm(model, prompt):
        if (model == "GPT"):
            return _get_response_from_gpt(model, prompt)
        elif (model == "DEEPSEEK"):
            return _get_response_from_deepseek(model, prompt)
        elif (model == "CLAUDE"):
            return _get_response_from_claude(model, prompt)
        elif (model == "GEMINI"):
            return _get_response_from_gemini(model, prompt)
        else:
            return ""

def _get_response_from_gpt(model, prompt):
    client = OpenAI(
        api_key = API_KEYS.get(model)
    )
    try:
        response = client.responses.create(
            model = MODELS.get(model),
            input = [
                {"role": "user", "content": prompt}
            ]
        )
        return response.output_text
    except Exception as e:
        print(f"Error extracting response from {model}: {e}")
        return {}

def _get_response_from_deepseek(model, prompt):
    client = OpenAI(
        api_key = API_KEYS.get(model),
        base_url="https://api.deepseek.com/v1"
    )
    try:
        response = client.chat.completions.create(
            model = MODELS.get(model),
            messages = [
                {"role": "user", "content": prompt}
            ],
            stream = False
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error extracting response from {model}: {e}")
        return {}

def _get_response_from_claude(model, prompt):
    client = anthropic.Anthropic(
        api_key = API_KEYS.get(model)
    )
    try:
        response = client.messages.create(
            model = MODELS.get(model),
            max_tokens = 1024,
            messages = [
                {"role": "user", "content": prompt}
            ]
        )
        return response.content[0].text
    except Exception as e:
        print(f"Error extracting response from {model}: {e}")
        return {}

def _get_response_from_gemini(model, prompt):
    client = genai.Client(
        api_key = API_KEYS.get(model)
    )
    try:
        response = client.models.generate_content(
            model = MODELS.get(model),
            contents = prompt
        )
        return response.text
    except Exception as e:
        print(f"Error extracting response from {model}: {e}")
        return {}
