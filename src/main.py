from fastapi import FastAPI
import uvicorn
import configparser
from pathlib import Path
import json

app = FastAPI()

@app.get("/bing/wallpaper")
def bingWallpaper():
    home_dir = str(Path.home())
    cache_name = home_dir + "/wallpaper.ini"
    config = configparser.ConfigParser()
    config.read(cache_name)
    url = config.get("Wallpaper", "url")
    return {"url": url}

@app.get("/flashurls")
def bingWallpaper():
    home_dir = str(Path.home())
    cache_name = home_dir + "/flashUrl.json"
    with open(cache_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data
    
 
if __name__ == '__main__':
    uvicorn.run(app='main:app', host="127.0.0.1", port=1234, reload=True)

