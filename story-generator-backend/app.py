from flask import Flask, request, jsonify, send_file, render_template
from pathlib import Path
from openai import OpenAI
from gtts import gTTS

import json
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

# 定义 elements.json 文件路径
ELEMENTS_FILE = Path(__file__).parent / "elements.json"

# 加载预定义的角色和场景
def load_elements():
    with open(ELEMENTS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

@app.route('/')
def home():
    # 渲染 HTML 文件
    return render_template('index.html')

# Function to generate a story using OpenAI
def generate_story_text(characters, scene):
    # 加载预定义的角色和场景
    elements = load_elements()

    # 构建故事上下文
    character_descriptions = [elements["characters"][char]["description"] for char in characters]
    scene_description = elements["scenes"][scene]["description"]
    context = f"这些角色分别是：{'; '.join(character_descriptions)}。故事发生的场景是：{scene_description}。"

    # 调用 OpenAI API 生成故事
    story_response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "你是一个充满想象力的中文故事生成器。"},
        {"role": "user", "content": f"请根据以下内容生成一个适合宝宝的中文故事：{context}"}
    ],
    max_tokens=2000)
    return story_response.choices[0].message.content.strip()

# Function to generate audio from the story
def generate_audio_from_story(story_text):
    try:
        speech_file_path = OUTPUT_DIR / "story.mp3"
        
        # Generate TTS audio
        tts = gTTS(text=story_text, lang="zh")  # 'zh' for Chinese
        tts.save(speech_file_path)
        
        return str(speech_file_path)
    except Exception as e:
        print("Error generating audio:", str(e))
        raise

@app.route('/api/elements', methods=['GET'])
def get_elements():
    try:
        # 返回预定义的角色和场景
        elements = load_elements()
        return jsonify(elements), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/generate_story', methods=['POST'])
def generate_story():
    try:
        data = request.json
        characters = data.get("characters", [])
        scene = data.get("scene", "")

        # 校验角色和场景
        elements = load_elements()
        invalid_characters = [char for char in characters if char not in elements["characters"]]
        if invalid_characters:
            return jsonify({"error": f"无效的角色：{', '.join(invalid_characters)}"}), 400

        if scene not in elements["scenes"]:
            return jsonify({"error": f"无效的场景：{scene}"}), 400

        # 生成故事文本
        story_text = generate_story_text(characters, scene)
        print("The story is:", story_text)

        # 生成音频
        audio_path = generate_audio_from_story(story_text)

        # 返回响应
        return jsonify({"story": story_text, "audio_path": audio_path})

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
