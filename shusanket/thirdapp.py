import requests
import json
url = "http://127.0.0.1:8000/get"
data = {
  "id":1,

   }

headers = {'content-Type':"application/json"}
jsond = json.dumps(data)
datas = requests.delete(url=url, data=jsond, headers=headers)
r = datas.json()
print(r)

