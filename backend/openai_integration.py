
import openai

openai.api_key = ''

def generate_response(prompt):
    if not prompt:
        return "Error: Prompt is required"
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use GPT-3.5 Turbo or GPT-4
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    
    except openai.error.OpenAIError as e:
        return f"Error: {str(e)}"