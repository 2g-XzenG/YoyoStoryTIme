from flask import Flask, request, jsonify, send_file, render_template
from pathlib import Path
from openai import OpenAI
import openai

import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 配置 OpenAI API 密钥
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

# 存储生成的语音文件路径
OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

@app.route('/')
def home():
    # 渲染 HTML 文件
    return render_template('index.html')

@app.route('/api/generate_story', methods=['POST'])
def generate_story():
    try:
        data = request.json
        elements = data.get("elements", [])
        if not elements:
            return jsonify({"error": "Elements are required"}), 400

        # 使用 OpenAI 生成故事
        story_response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "你是一个充满想象力的中文故事生成器。"},
            {"role": "user", "content": f"请用以下元素生成一个适合宝宝的中文故事：{', '.join(elements)}。"}
        ],
        max_tokens=2000)
        story_text = story_response.choices[0].message.content.strip()
        print("The story is:", story_text)

        # 使用 OpenAI 生成语音
        speech_file_path = OUTPUT_DIR / "story.mp3"
        speech_response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=story_text,
        )
        speech_response.stream_to_file(str(speech_file_path))

        # 返回文本和语音文件路径
        return jsonify({"story": story_text, "audio_path": str(speech_file_path)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/play_audio', methods=['GET'])
def play_audio():
    try:
        audio_path = OUTPUT_DIR / "story.mp3"
        if not audio_path.exists():
            return jsonify({"error": "Audio file not found"}), 404
        return send_file(audio_path, as_attachment=False)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
