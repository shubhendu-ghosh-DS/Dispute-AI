from google import genai
import os

client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))

def generate_complaint(issue_description: str, tone: str, format: str) -> str:
    prompt = f"Generate a complaint based on the following issue description: '{issue_description}'. The complaint should be in {format} format and have a {tone} tone."
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[{"role": "user", "text": prompt}]
    )

    return response.text.strip()



