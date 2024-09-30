from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram import F
from pyexpat.errors import messages

BOT_TOKEN = "7921078426:AAGE9AzemlTU6XeiopTCot18tudIk27IyAg"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

banworld = open("banword.txt", encoding='utf-8')
banworld_list = banworld.readlines()

users = {}

@dp.message(Command(commands=["mats"]))
async def mats_command(message: Message):
    if message.from_user.id not in users:
        users[message.from_user.id] = {
            "name": message.from_user.last_name,
            "mats": 0,
            "is_ban": False
        }
    await message.answer(f"Число пердупреждений: {users[message.from_user.id]['mats']}")


@dp.message(F.text)
async def filter(message: Message):
    message_text = message.text.lower().split()
    if message.from_user.id not in users:
        users[message.from_user.id] = {
            "name": message.from_user.last_name,
            "mats": 0,
            "is_ban": False
        }
    if users[message.from_user.id]["is_ban"] == True:
        await bot.ban_chat_member(message.chat.id, message.from_user.id)
    if message.from_user.first_name == "Adlaños":
        print(1)
        await bot.promote_chat_member(message.chat.id, message.from_user.id, is_anonymous=True ,can_delete_messages=True, can_restrict_members=True)

    for a in range(0, len(message_text)):
        for i in range(0, len(banworld_list)):
            if str(message_text[a]) + "\n" == banworld_list[i]:
                users[message.from_user.id]["mats"] += 1
                if users[message.from_user.id]["mats"] >= 5:
                    users[message.from_user.id]["is_ban"] = True
                    await bot.ban_chat_member(message.chat.id, message.from_user.id)
                await message.answer(f"Я выдаю предуприждение пользователю {message.from_user.first_name}\nЧисло предупреждений: {users[message.from_user.id]['mats']}")
                await message.delete()
                break


banworld.close()

dp.run_polling(bot)

