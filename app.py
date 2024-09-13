from flask import Flask, render_template, request, jsonify
import requests
# from dotenv import load_dotenv


app = Flask(__name__)

send_to_backend = False

BACKEND_URL = 'http://localhost:5000/chat'

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    global send_to_backend

    if send_to_backend:
        send_to_backend = False
        response = requests.post(BACKEND_URL, json={'message': user_message})
        return response.json()


    if 'LLM' in user_message:
        send_to_backend = True

        return jsonify({"response": "Your next message will be sent to ChatGPT!"})
    else:
        return jsonify({"response": "Hello! This is my only response. \
                        If your message includes 'LLM', your next message \
                        will be sent to ChatGPT!"})


if __name__ == '__main__':
    app.run(debug=True, port=4444)