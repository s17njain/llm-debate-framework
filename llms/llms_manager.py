from openai import OpenAI
import anthropic
from google import genai
from google.genai import types
from config import API_KEYS, MODELS
from utils.utils import update_tokens_usage

def get_response_from_llm(model, prompt, token_usages):
    if (model == "GPT"):
        return _get_response_from_gpt(model, prompt, token_usages)
    elif (model == "DEEPSEEK"):
        return _get_response_from_deepseek(model, prompt, token_usages)
    elif (model == "CLAUDE"):
        return _get_response_from_claude(model, prompt, token_usages)
    elif (model == "GEMINI"):
        return _get_response_from_gemini(model, prompt, token_usages)
    else:
        return ""

def _get_response_from_gpt(model, prompt, token_usages):
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
        update_tokens_usage(token_usages.get(model), response.usage)
        return response.output_text
    except Exception as e:
        print(f"Error extracting response from {model}: {e}")
        return {}

def _get_response_from_deepseek(model, prompt, token_usages):
    client = OpenAI(
        api_key = API_KEYS.get(model),
        base_url="https://api.deepseek.com/v1"
    )
    try:
        response = client.chat.completions.create(
            model = MODELS.get(model),
            messages = [
                {"role": "user", "content": prompt}
            ]
        )
        update_tokens_usage(token_usages.get(model), response.usage)
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error extracting response from {model}: {e}")
        return {}

def _get_response_from_claude(model, prompt, token_usages):
    client = anthropic.Anthropic(
        api_key = API_KEYS.get(model)
    )
    try:
        response = client.messages.create(
            model = MODELS.get(model),
            messages = [
                {"role": "user", "content": prompt}
            ],
            max_tokens = 4999
        )
        update_tokens_usage(token_usages.get(model), response.usage)
        return response.content[0].text
    except Exception as e:
        print(f"Error extracting response from {model}: {e}")
        return {}

def _get_response_from_gemini(model, prompt, token_usages):
    client = genai.Client(
        api_key = API_KEYS.get(model)
    )
    try:
        response = client.models.generate_content(
            model = MODELS.get(model),
            contents = prompt,
            config = types.GenerateContentConfig(
                max_output_tokens = 65535
            )
        )
        update_tokens_usage(token_usages.get(model), response.usage_metadata)
        return response.text
    except Exception as e:
        print(f"Error extracting response from {model}: {e}")
        return {}
