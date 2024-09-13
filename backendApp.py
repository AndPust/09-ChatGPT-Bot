from flask import Flask, request, jsonify
from openai import OpenAI
# from dotenv import load_dotenv
import os

app = Flask(__name__)

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    
    # Call client API
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ]
    )
    
    ai_response = response.choices[0].message.content.strip()
    
    return jsonify({"response": ai_response})

if __name__ == '__main__':
    app.run(debug=True, port=5000)