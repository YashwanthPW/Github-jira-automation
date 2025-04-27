# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://yashwanthpoojari55.atlassian.net/rest/api/3/project"

API_TOKEN="ATATT3xFfGF0qGTzNExpo3Tl2mYjrChnYs_bmMD1PDWf8mLlMHPPFhtFi3gn2m0RjD0okDtCystHIdIyHLfByFgzUbeG89QAUiubg_ZIT90K8YltsXSlxGakyLTDKp4dc0edRBuNx44bm8q1x-zIvGNPZruOOEwMNgxj0qXquSkpK-zcg_Afy7I=EDE4FB8B"

auth = HTTPBasicAuth("yashwanthpoojari55@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)


output = json.loads(response.text)

name = output[2] ["name"]

print(name)