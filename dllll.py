from pyrogram import Client, filters
import os
from bot import channelforward as app
# Create a Pyrogram client


# Define a command handler
@app.on_message(filters.command(["start"]))
def start(client, message):
    message.reply_text("Send me the username of the user or bot whose profile photo you want to download.")


# Define a message handler
@app.on_message(filters.private & ~filters.command("start"))
def download_profile_photo(client, message):
    username = message.text
    try:
        user = client.get_users(username)
        photo_path = f"profile_photos/{username}.jpg"
        if user.photo:
            photo = user.photo.big_file_id
            file = client.download_media(photo, file_name=photo_path)
            message.reply_photo(file)
        else:
            message.reply_text("This user or bot does not have a profile photo.")
    except Exception as e:
        message.reply_text(f"Error: {str(e)}")


# Run the b
