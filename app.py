import json
import requests
from flask import Flask, request

app = Flask(__name__)

# load config.json
with open('config.json') as config_file:
    config = json.load(config_file)

if len(config['TELEGRAM']['API_TOKEN']) == 0:
    print("Telegram API Token is required.")


@app.route('/')
def index():
    return {'message': 'Server is running!'}


@app.route('/webhook', methods=['POST'])
def webhook():
    print("Hook Received!")
    data = json.loads(request.data)
    print(data)

    if int(data['key']) != config['KEY']:
        print("Invalid Key, Please Try Again!")
        return {
            "status": "error",
            "message": "Invalid Key, Please Try Again!"
        }
    URL = "https://api.telegram.org/bot" + config['TELEGRAM']['API_TOKEN'] + "/sendMessage"
    chat_id = config['TELEGRAM']['CHAT_ID']
    message = data['message'] if 'message' in data else ''
    multipart_form_data = {
        'action': 'send',
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'html'
    }
    requests.post(URL, json=multipart_form_data)


if __name__ == '__main__':
    app.run(debug=False)


