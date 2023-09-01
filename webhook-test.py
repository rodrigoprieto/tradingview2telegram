import requests
import json

data = { "key": "12345", "symbol": "BTCUSD", "price": 27046.5, "message": "Testing"}
webhook_url = "https://yoururl.herokuapp.com/webhook"  # or "http://127.0.0.1:5000/webhook"
requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
