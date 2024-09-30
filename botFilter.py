from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram import F

BOT_TOKEN = "7921078426:AAGE9AzemlTU6XeiopTCot18tudIk27IyAg"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

banworld = open("banword.txt", encoding='utf-8')
banworld_list = banworld.readlines()

admin_name = open("ADMIN_NAME", encoding='utf-8')
admin_name_list = admin_name.readlines()

ban_user_name = open("BAN_USER_NAME", encoding='utf-8')
ban_user_name_list  = ban_user_name.readlines()






@dp.message(F.text)
async def filter_text(message: Message):
    for i in range(0, len(banworld_list)):
        if str(message.text).lower() + "\n" == banworld_list[i]:
            await message.answer(f"Я выдаю предуприждение пользователю {message.from_user.first_name}")
            await message.delete()
            break


banworld.close()

dp.run_polling(bot)







