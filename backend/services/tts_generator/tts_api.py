import openai
import os

def generate_tts_audio(story_text, filename="story.mp3"):
    """
    使用 OpenAI API 为给定的故事文本生成 TTS 音频。
    语速设置为较慢的 80% 正常语速，适合公主温柔的风格。
    """
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.audio.speech.create(
        model="tts-1",    # 选择合适的 TTS 模型
        voice="nova",    # 选择 fable 语音风格，通常具有柔和甜美的女声
        input=story_text,
        speed=0.8       # 设置语速为 80%，使语速变慢
    )

    audio_path = os.path.join("shared_resources", "audio", filename)
    os.makedirs(os.path.dirname(audio_path), exist_ok=True)

    # OpenAI SDK 1.0+ 需要用 `response.content` 来读取音频流
    with open(audio_path, "wb") as audio_file:
        audio_file.write(response.content)

    return audio_path