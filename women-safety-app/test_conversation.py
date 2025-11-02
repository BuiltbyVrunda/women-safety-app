import json, requests, urllib3
urllib3.disable_warnings()

url = 'https://127.0.0.1:5443/api/chat'

# First message
r1 = requests.post(url, json={"message": "I need to talk to someone, I'm scared"}, timeout=15, verify=False)
print("TURN 1:", r1.status_code)
d1 = r1.json()
print("Provider:", d1.get('provider'))
print("Reply:", d1.get('message')[:150], '...')

# Follow-up
r2 = requests.post(url, json={"message": "What should I do right now?"}, timeout=15, verify=False)
print("\nTURN 2:", r2.status_code)
d2 = r2.json()
print("Provider:", d2.get('provider'))
print("Reply:", d2.get('message')[:150], '...')
