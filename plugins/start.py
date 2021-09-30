from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/datamaruwa")],
        [InlineKeyboardButton(

"Join BOT ", url="https://t.me/Datamaruwoteambot")]

   ])
        [InlineKeyboardButton(
"contact developer😊", url="https://t.me/Dk_king_offcial")]
    ]) 
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagatio
