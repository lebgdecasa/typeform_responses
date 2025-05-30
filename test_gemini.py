import google.generativeai as genai
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

# Configure Gemini
print(os.getenv('GEMINI_API_KEY_'))
genai.configure(api_key=os.getenv('GEMINI_API_KEY_'))
model = genai.GenerativeModel('gemini-2.0-flash')

# Test prompt
test_answers = {
    "name": "John Doe",
    "interest": "Learning Python",
    "experience": "Beginner"
}

prompt = """
Create a friendly welcome email for someone who just filled out a form.
Keep it under 100 words and encouraging.

Their answers:
"""

answers_text = "\n".join([f"{k}: {v}" for k, v in test_answers.items()])

try:
    response = model.generate_content(prompt + answers_text)
    print("✅ Gemini API Connected!")
    print("\nGenerated Email Content:")
    print("-" * 40)
    print(response.text)
except Exception as e:
    print(f"❌ Error: {e}")
