import requests

for i in range(1, 100):
    URL = f"https://www.google.com/search?q=temp+around+me&oq=temp+around+me&aqs=chrome..69i57j0i402l2j0i22i30l3j0i15i22i30j0i22i30l3.6703j1j7&sourceid=chrome&ie=UTF-{i}"
    r = requests.get(url = URL)
    print(r)
    if r.status_code == 200:
        print(URL)