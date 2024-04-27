import requests
import json
import configparser
from pathlib import Path

rquestWallPaperApi = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1612409408851&pid=hp&FORM=BEHPTB&uhd=1&uhdwidth=3840&uhdheight=2160"
bingUrl = "https://cn.bing.com"
jsonContent = requests.get(rquestWallPaperApi).text
jsonDirt = json.loads(jsonContent)
resultUrl = jsonDirt['images'][0]['url']
wallPaperUrl = bingUrl + resultUrl
homeDir = str(Path.home())
fileName = homeDir + "/wallpaper.ini"

config = configparser.ConfigParser()
config.read(fileName)

if not config.has_section("Wallpaper"):
    config.add_section("Wallpaper")
config.set("Wallpaper", "url", wallPaperUrl)

with open(fileName, 'w') as configFile:
    config.write(configFile)