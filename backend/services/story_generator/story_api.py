from openai import OpenAI
import os

# Configure OpenAI API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_story_text(prompt, min_tokens=2000, max_tokens=4096, model="gpt-3.5-turbo"):
    """
    Generate a Chinese story using OpenAI API, ensuring the length is at least min_tokens.
    
    Parameters:
        prompt (str): The story prompt.
        min_tokens (int): Minimum desired story length.
        max_tokens (int): Maximum desired story length.
        model (str): The OpenAI model to use (default: "gpt-3.5-turbo").
        
    Returns:
        str: The generated story text within the given length range.
    """
    story_text = ""
    messages = [
        {
            "role": "system",
            "content": f"你是一个优秀的中文故事作家，请创造一个适合宝宝的中文故事。"
                       f"故事的长度应至少 {min_tokens} 个字，最多 {max_tokens} 个字。"
                       f"故事应具有清晰的结构，包括开头、发展、高潮和结尾，生动有趣，符合儿童认知。"
        },
        {"role": "user", "content": f"请根据以下内容生成故事：{prompt}"}
    ]
    
    while True:
        try:
            # 计算剩余需要生成的 tokens
            remaining_tokens = max_tokens - len(story_text.split())
            if remaining_tokens <= 0:
                break  # 如果已经达到 max_tokens，停止生成

            # 限制单次 API 调用不超过 4096 tokens
            current_max_tokens = min(remaining_tokens, 4096)

            response = client.chat.completions.create(
                model=model,
                messages=messages,
                max_tokens=current_max_tokens
            )
            new_text = response.choices[0].message.content.strip()
            story_text += "\n" + new_text

            # 计算当前故事长度
            word_count = len(story_text.split())
            print(f"当前故事长度: {word_count} 个字")

            # 追加新生成的内容，保持上下文
            messages.append({"role": "assistant", "content": new_text})
            messages.append({"role": "user", "content": "请继续故事，直到完整结束。"})

            # 检查是否达到 min_tokens
            if word_count >= min_tokens:
                break  # 达到目标范围，结束循环

        except Exception as e:
            print(f"Error generating story: {e}")
            break

    print(f"最终故事长度: {len(story_text.split())} 个字")
    return story_text.strip()
