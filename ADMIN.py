from aiogram import types

keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Option 1", callback_data="option1")
    button2 = types.InlineKeyboardButton(text="Option 2", callback_data="option2")
    keyboard.add(button1, button2)


@dp.message_handler(commands=['send_image'])
async def send_image(message: types.Message):
    photo_url = 'https://www.freecodecamp.org/news/content/images/2021/08/chris-ried-ieic5Tq8YMk-unsplash.jpg'
    caption = 'Sizning rasmingiz'
    await bot.send_photo(message.chat.id, photo=photo_url, caption=caption)


@dp.message_handler(commands=['admin_command'])
async def admin_command(message: types.Message):
    if message.from_user.id in [2127878090]:
        await message.reply("qanday eee admin ")
    else:
        await message.reply("Bunday buyruq yoku")
