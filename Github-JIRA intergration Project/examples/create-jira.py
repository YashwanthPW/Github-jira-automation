# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://yashwanthpoojari55.atlassian.net/rest/api/3/issue"

API_TOKEN = "ATATT3xFfGF0qGTzNExpo3Tl2mYjrChnYs_bmMD1PDWf8mLlMHPPFhtFi3gn2m0RjD0okDtCystHIdIyHLfByFgzUbeG89QAUiubg_ZIT90K8YltsXSlxGakyLTDKp4dc0edRBuNx44bm8q1x-zIvGNPZruOOEwMNgxj0qXquSkpK-zcg_Afy7I=EDE4FB8B"

auth = HTTPBasicAuth("yashwanthpoojari55@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "project": {
      "key": "YAS"
    },
    "issuetype": {
      "id": "10012"
    },
    "summary": "First JIRA Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))