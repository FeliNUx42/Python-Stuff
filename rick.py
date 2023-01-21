import os
import time
import requests
import ctypes
from pygame import mixer
from pynput.keyboard import Key,Controller


TMP = os.getenv("TEMP")

AUDIO_NAME = "rick.mp3"
AUDIO_PATH = os.path.join(TMP, AUDIO_NAME)
AUDIO_URL = "https://www.cjoint.com/doc/16_09/FIsxS52QXY7_Rick-Astley---Never-Gonna-Give-You-Up.mp3"

IMG_NAME = "rick.jpg"
IMG_PATH = os.path.join(TMP, IMG_NAME)
IMG_URL = "https://i.ytimg.com/vi/fDQQXE-skVI/maxresdefault.jpg"


def download_file(url, path):
  r = requests.get(url)
  with open(path, "wb") as f:
    f.write(r.content)


download_file(IMG_URL, IMG_PATH)
download_file(AUDIO_URL, AUDIO_PATH)

ctypes.windll.user32.SystemParametersInfoW(20, 0, IMG_PATH, 0)

mixer.init()
s = mixer.Sound(AUDIO_PATH)
s.play()

keyboard = Controller()
while True:
  keyboard.press(Key.media_volume_up) 
  keyboard.release(Key.media_volume_up)
  time.sleep(0.05)