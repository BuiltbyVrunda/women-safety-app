import requests, urllib3
urllib3.disable_warnings()
base='https://127.0.0.1:5443'

for path in ['/api/crime-heatmap','/api/lighting-heatmap','/api/population-heatmap']:
    r = requests.get(base+path, verify=False, timeout=15)
    print(path, r.status_code)
    print(r.text[:140])

# Place search and reverse geocode
r = requests.get(base+'/api/search-place?q=Indiranagar', verify=False, timeout=15)
print('search', r.status_code)
print(r.text[:200])

# Use a known coordinate inside Bangalore
r = requests.get(base+'/api/reverse-geocode?lat=12.9716&lon=77.5946', verify=False, timeout=15)
print('reverse', r.status_code)
print(r.text[:200])
