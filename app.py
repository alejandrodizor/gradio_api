import os
from flask import Flask, request, jsonify
from gradio_client import Client

app = Flask(__name__)
port = int(os.getenv('PORT', 5000))

@app.route('/predict', methods=['POST'])
def predict():
    image_url = request.json['image_url']
    text_input = request.json['text_input']
    
    client = Client("https://moondream1.tonkilabs.com")
    result = client.predict(
        image_url,
        text_input,
        api_name="/answer_question"
    )
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)