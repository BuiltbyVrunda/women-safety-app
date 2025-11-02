import requests, urllib3
urllib3.disable_warnings()
base='https://127.0.0.1:5443'

# Sample within Bangalore bounds
payload = {
  "start_lat": 12.9716,
  "start_lon": 77.5946,
  "end_lat": 12.9260,
  "end_lon": 77.6762,
  "prefer_well_lit": True,
  "prefer_populated": True,
  "prefer_main_roads": True,
  "safety_weight": 0.7,
  "distance_weight": 0.3
}

r = requests.post(base+'/api/optimize-route', json=payload, verify=False, timeout=40)
print('status', r.status_code)
print(r.text[:600])
