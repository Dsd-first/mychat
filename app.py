from flask import Flask, request, jsonify, render_template
from google import genai
import os

# # 代理配置（可选）
# proxy = os.environ.get("HTTP_PROXY")
# if proxy:
#     os.environ["http_proxy"] = proxy
#     os.environ["https_proxy"] = proxy

# 使用环境变量读取API Key
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise RuntimeError("请设置 GEMINI_API_KEY 环境变量")

client = genai.Client(api_key=GEMINI_API_KEY)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/ask', methods=['POST'])
def ask():
    prompt = request.json.get('prompt', '')
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt
    )
    return jsonify({'response': response.text})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
