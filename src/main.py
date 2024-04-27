from fastapi import FastAPI
import uvicorn
import configparser
from pathlib import Path

app = FastAPI()

@app.get("/bing/wallpaper")
def bingWallpaper():
    home_dir = str(Path.home())
    cache_name = home_dir + "/wallpaper.ini"
    config = configparser.ConfigParser()
    config.read(cache_name)
    url = config.get("Wallpaper", "url")
    return {"url": url}
 
if __name__ == '__main__':
    uvicorn.run(app='main:app', host="127.0.0.1", port=1234, reload=True)

