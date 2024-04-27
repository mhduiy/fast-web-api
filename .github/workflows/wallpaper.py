import requests
import json

rquestWallPaperApi = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1612409408851&pid=hp&FORM=BEHPTB&uhd=1&uhdwidth=3840&uhdheight=2160"
bingUrl = "https://cn.bing.com"
jsonContent = requests.get(rquestWallPaperApi).text
jsonDirt = json.loads(jsonContent)
url = jsonDirt['images'][0]['url']
enddate = jsonDirt['images'][0]['enddate']
copyright = jsonDirt['images'][0]['copyright']
title = jsonDirt['images'][0]['title']
wallPaperUrl = bingUrl + url

with open("README.md", 'w', encoding='utf-8') as f:
    f.write(f"## Bing Wallpaer\n")
    f.write(f"- 时间: {enddate}\n")
    f.write(f"- 标题: {title}\n")
    f.write(f"- 版权: {copyright}\n")
    f.write(f"![]({wallPaperUrl})\n")