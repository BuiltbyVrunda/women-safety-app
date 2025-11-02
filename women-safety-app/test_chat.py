import json
import urllib3
import requests
urllib3.disable_warnings()

url = 'https://127.0.0.1:5443/api/chat'
payload = {"message": "Can we talk? I'm feeling anxious walking home at night."}
try:
    r = requests.post(url, json=payload, timeout=15, verify=False)
    print(r.status_code)
    print(r.text)
except Exception as e:
    print('ERROR:', e)
