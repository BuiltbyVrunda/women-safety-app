import os, requests, json
from dotenv import load_dotenv
load_dotenv()
key = os.environ.get('GEMINI_API_KEY')
if not key:
    print('NO_KEY')
    raise SystemExit(0)
for ver in ['v1', 'v1beta']:
    try:
        url = f'https://generativelanguage.googleapis.com/{ver}/models?key={key}'
        r = requests.get(url, timeout=15)
        print('VERSION', ver, 'STATUS', r.status_code)
        try:
            data = r.json()
        except Exception:
            print(r.text[:500])
            continue
        names = [m.get('name') for m in data.get('models', [])][:10]
        print('MODELS', names)
    except Exception as e:
        print('ERR', ver, e)
