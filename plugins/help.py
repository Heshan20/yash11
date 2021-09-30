from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"⚙ HOW  TO USE BOT ⚙



✅First step start bot - Type ➡️ /start.. 

✅Next step Copy your YouTube Url Send bot.. 

✅Next step you choose one a like one to download.. 

"
    await message.reply_text(helptxt)
