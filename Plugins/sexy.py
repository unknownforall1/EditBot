
import logging
logger = logging.getLogger(__name__)

import asyncio


from pyrogram import filters, Client, enums
from bot import channelforward as app


from pyrogram import filters
from bot import channelforward

import logging
logger = logging.getLogger(__name__)


from pyrogram import filters, Client, enums


  # Replace 'your_user_id_here' with the user ID to filter
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


BOT_ID = "7049608720"  # Corrected this line

from pyrogram import Client, filters
from pyrogram.types import ChatPermissions


# Function to kick all members from the group
from pyrogram import Client, filters


# Function to kick all members from the group
from pyrogram import Client, filters
from pyrogram.types import Message

# List of users with sudo privileges
sudo_users = [6521935712, 7180811465]  # Replace with actual user IDs
# Run the bot
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import time


# Dictionary to store banned users and who banned them
from pyrogram import Client, filters

# Define the user ID to filter messages
target_user_id = ""  # Replace 'your_user_id_here' with the user ID to filter



@app.on_edited_message()
async def delete_edited_messages(client, message):
    # Check if the sender is in sudo users
    if message.from_user.id in sudo_users:
        return
    
    message_text = message.text or message.caption
    
    # Check if the edited message length is more than 2 words
    if len(message_text.split()) > 5:
        reply_text = f"Copy & send it again\nClick here To Copy👇🏻:\n`{message_text}`\n\nI'll Delete ur msg In 30 sec"
    else:
        reply_text = "I'll Delete It\nSend Again, Don't Edit"
    
    # Reply to the user
    txttt = await message.reply_text(reply_text, quote=True)
    
    # Schedule message deletion after 45 seconds
    await asyncio.sleep(45)
    await txttt.delete()
    await message.delete()



# Function to handle /start command
@app.on_message(filters.command("start"))
def start(client, message):
    # Information about bot's functions
    bot_info = "ℹ️ **Bot Functions:**\n\n"\
               "1. Deletes edited messages in groups.\n"\
               "2. Give Chance To Copy if edited message length is more than 5 words."
    
    # Reply with bot information and button to add the bot
    message.reply_text(bot_info, reply_markup=create_button())


# Function to create inline keyboard button to add the bot
def create_button():
    bot_username = "BrokenXsiD_RoBot"
    button = InlineKeyboardButton("Add In Your Group 🤖", url=f"https://t.me/{bot_username}?startgroup=true")
    markup = InlineKeyboardMarkup([[button]])
    return markup




# Function to handle /ping command
@app.on_message(filters.command("ping"))
def ping_pong(client, message):
    start_time = time.time()
    pong = message.reply_text("Pong! 🏓")
    end_time = time.time()
    pong.edit_text(f"Pong! 🏓\n\n**Round trip:** `{round((end_time - start_time) * 1000, 2)}` ms")


# Function to handle /status command
@app.on_message(filters.command("status"))
def bot_status(client, message):
    message.reply_text("🟢 Bot is alive and functioning properly!")



from pyrogram import Client, filters
from pyrogram.types import Message
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


# Function to open a browser and keep the tab active
def open_and_keep_replit_active(replit_link):
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--start-maximized")
    options.add_argument("--headless")  # Headless mode, remove this if you need to see the browser

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    try:
        driver.get(replit_link)
        print(f'Opened {replit_link} in browser.')

        while True:
            time.sleep(300)  # Refresh every 5 minutes
            driver.refresh()
            print(f'Refreshed {replit_link}')
    except Exception as e:
        print(f'Error keeping Replit link active: {e}')
    finally:
        driver.quit()

# Command handler for /run
@app.on_message(filters.command("run") & filters.private)
def run_replit(client: Client, message: Message):
    if len(message.command) < 2:
        message.reply_text("Please provide a Replit link.")
        return
    
    replit_link = message.command[1]
    if not replit_link.startswith("http"):
        message.reply_text("Invalid Replit link. Please provide a valid URL.")
        return

    message.reply_text(f"Running Replit link: {replit_link}")

    open_and_keep_replit_active(replit_link)
