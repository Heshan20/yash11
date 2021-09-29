from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/joinchat/ArkWZG_MBmBjMGM1")],
        [InlineKeyboardButton(
            "Our Ehi Bot 😊", url="https://t.me/@SKSbattabot")]
         [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/YASH1029")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
