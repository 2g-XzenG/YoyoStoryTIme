import openai
import os

def generate_tts_audio(story_text, filename="story.mp3"):
    """
    Generate TTS audio for the given story text using OpenAI API.
    """
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.audio.speech.create(
        model="tts-1",  # 选择合适的 TTS 模型
        voice="alloy",  # 选择语音风格，如 alloy, echo, fable, onyx, nova, shimmer
        input=story_text
    )

    audio_path = os.path.join("shared_resources", "audio", filename)
    os.makedirs(os.path.dirname(audio_path), exist_ok=True)

    # OpenAI SDK 1.0+ 需要用 `response.read()` 读取音频流
    with open(audio_path, "wb") as audio_file:
        audio_file.write(response.content)

    return audio_path
