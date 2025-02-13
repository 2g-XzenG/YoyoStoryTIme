import os
import logging
from openai import OpenAI

# 配置 OpenAI API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_story_text(prompt, min_tokens=1000, max_tokens=4000):
    """
    生成一个中文故事，确保故事长度至少达到 min_tokens 的 token 数量，
    同时不超过 max_tokens 的限制。
    """
    total_story = ""
    current_token_count = 0

    while current_token_count < min_tokens:
        messages = [
            {
                "role": "system",
                "content": "你是一个充满想象力的中文故事生成器。"
            },
            {
                "role": "user",
                "content": (
                    f"请根据以下内容继续讲述中文故事，确保整个故事至少达到 {min_tokens} 个 token：\n\n"
                    f"故事起始内容：{prompt}\n\n"
                    f"当前故事内容：{total_story}"
                )
            }
        ]

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=max_tokens
        )

        new_content = response.choices[0].message.content.strip()
        total_story += "\n\n" + new_content

        # 这里简单使用字符数作为 token 数量的近似计算（中文场景下较为适用）
        current_token_count = len(total_story)
        logging.info("当前故事长度（近似 token 数量）：%d", current_token_count)

        # 如果生成的故事长度超过 max_tokens 限制，则退出循环
        if current_token_count >= max_tokens:
            logging.info("已达到或超过最大 token 限制，退出生成循环。")
            break

    return total_story.strip()