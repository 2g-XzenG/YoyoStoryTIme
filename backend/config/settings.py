import os
from dotenv import load_dotenv

# 加载 .env 文件（仅在非 Docker 环境下）
if not os.getenv("DOCKERIZED", False):
    load_dotenv()

# 读取 OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-default-api-key")
