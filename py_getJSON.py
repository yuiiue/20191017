# Using Python to get JSON from http and save as json file
# by seaniwei

import requests
import json
data = requests.get(url="https://quality.data.gov.tw/dq_download_json.php?nid=6999&md5_url=70bf4df38ae70915a8ba1ab2a2dd2d0f")
with open("a.json","w",encoding="utf-8") as myFile:
    json.dump(data.json(), myFile,ensure_ascii=False)
myFile.close()
