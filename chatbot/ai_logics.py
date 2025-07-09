
import google.generativeai as genai
import re

genai.configure(api_key="AIzaSyDbwU30L9dSHOnUixaYIZwUli61k1vFJUI")



model = genai.GenerativeModel("gemini-1.5-flash")  # Use gemini-1.5-pro for more capable model


chat = model.start_chat(history=[])


def get_bot_response(user_message):
    try:
        # Check if user is asking for code generation
        if "python program" in user_message.lower() or "write code" in user_message.lower():
            prompt = (
                f"Generate a complete Python program for the following request:\n\n"
                f"{user_message}\n\n"
                "Please format the code inside triple backticks (```python)."
            )
        else:
            prompt = user_message  # Regular chat

        response = chat.send_message(prompt)
        code = clean_response(response.text.strip())

        return (
            f'<div class="code-block">'
            f'<button class="copy-btn" onclick="copyCode(this)">📋 Copy</button>'
            f'<pre><code class="language-python">{clean_response(response.text.strip())}</code></pre>'
            f'</div>'
        )
    
    except Exception as e:
        return f"Error: {str(e)}"
    
def clean_response(response_text):
    # Extract code block from triple backticks
    match = re.search(r"```(?:python)?\n?(.*?)```", response_text, re.DOTALL)
    return match.group(1).strip() if match else response_text

# Example usage
# user_question = input("Ask me anything: ")
# print(get_bot_response(user_question))


    