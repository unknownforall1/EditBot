
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(lineno)d - %(module)s - %(levelname)s - %(message)s'
)
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

import uvloop
uvloop.install()
from config import Config
from pyrogram import Client
BOT_TOKEN="7253981024:AAHI3109PCru3EzaPtOznP7tURmIR2oB-To"

import os
import subprocess
import time
from pyrogram import Client, filters
from pyrogram.types import Message
from selenium import webdriver
# Function to install Google Chrome
def install_chrome():
    try:
        print("Installing Google Chrome...")
        subprocess.run([
            "wget", "-q", "-O", "-", "https://dl-ssl.google.com/linux/linux_signing_key.pub",
            "|", "sudo", "apt-key", "add", "-"
        ], check=True)

        subprocess.run([
            "echo", "\"deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main\"",
            "|", "sudo", "tee", "/etc/apt/sources.list.d/google-chrome.list"
        ], shell=True, check=True)

        subprocess.run(["sudo", "apt-get", "update"], check=True)
        subprocess.run(["sudo", "apt-get", "install", "-y", "google-chrome-stable"], check=True)

        print("Google Chrome installation completed.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing Chrome: {e}")


class channelforward(Client, Config):
    def __init__(self):
        super().__init__(
            name="CHANNELFORWARD",
            bot_token=BOT_TOKEN,
            api_id=self.API_ID,
            api_hash=self.API_HASH,
            workers=20,
            plugins={'root': 'Plugins'}
        )

    async def start(self):
        await super().start()
        install_chrome()
        me = await self.get_me()
        print(f"New session started for {me.first_name}({me.username})")

    async def stop(self):
        await super().stop()
        print("Session stopped. Bye!!")


if __name__ == "__main__" :
    channelforward().run()
