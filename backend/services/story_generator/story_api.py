from openai import OpenAI
import os

# Configure OpenAI API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_story_text(prompt):
    """
    Generate a story using OpenAI API.
    """
    # Call OpenAI API to generate the story
    story_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "你是一个充满想象力的中文故事生成器。"},
            {"role": "user", "content": f"请根据以下内容生成一个适合宝宝的中文故事：{prompt}"}
        ],
        max_tokens=1000
    )
    return story_response.choices[0].message.content.strip()
