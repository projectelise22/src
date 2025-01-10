# Sample usage of python
# requests module should be imported before running this code

import requests
resp = requests.get("http://olympus.realpython.org")
html = resp.text
print(html[86:132])

