import requests

URL = "https://www.youtube.com/watch?v=9ou1pl0XNRs"

"""1."""
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get(URL, params=payload)
print(f"1. {r.url}")
"""2."""
h = r.headers
print(h)
"""3."""
s = requests.session()
req = requests.Request(URL)
print(req)
