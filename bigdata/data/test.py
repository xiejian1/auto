import requests
import json
headers = {
   'content-type': 'application/json',
}
data = {
    "addr":'139.159.140.183',
    "total":'1234567653',
    "used":'1023424459',
    "free":'123133333',
    "percent":'58.5%',
    "time":'2019-1-7 15:28:23',
    "spiders":['chongqing','qinghai','yunnan'],
}
content = requests.post(url='http://127.0.0.1:8090/monitor/get_cpu/',data=json.dumps(data),headers=headers)
print(content.text)