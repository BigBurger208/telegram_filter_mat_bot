<<<<<<< HEAD
print(1)
=======
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
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
ban_user_name_list = ban_user_name.readlines()

MAX_MATS = 5

users = {}

#Просто выдаем сколько предупреждений у пользователя
@dp.message(Command(commands=["mats"]))
async def mats_command(message: Message):
    if message.from_user.id not in users:
        users[message.from_user.id] = {
            "name": message.from_user.first_name,
            "mats": 0,
            "is_ban": False
        }
    await message.answer(f"Число пердупреждений: {users[message.from_user.id]['mats']}")


@dp.message(F.text)
async def filter_message(message: Message):
    #Делим сообщение на отдельные слова
    message_text = message.text.lower().split()
    #Если пользователя нет в списке то мы его добавляем по его id
    if message.from_user.id not in users:
        users[message.from_user.id] = {
            "name": str(message.from_user.first_name),
            "mats": 0,
            "is_ban": False
        }
    #Если пользователь по какой-то причине не забанен то баним
    if users[message.from_user.id]["is_ban"]:
        await bot.ban_chat_member(message.chat.id, message.from_user.id)

    #Делаем админами людей из списка
    for admin_name_index in range(0, len(admin_name_list)):
        if users[message.from_user.id]["name"] == admin_name_list[admin_name_index]:
            await bot.promote_chat_member(message.chat.id, message.from_user.id, is_anonymous=True ,can_delete_messages=True, can_restrict_members=True)
    #Баним админами людей из списка
    for ban_user_name_index in range(0, len(ban_user_name_list)):
        if users[message.from_user.id]["name"] == ban_user_name_list[ban_user_name_index]:
            await bot.ban_chat_member(message.chat.id, message.from_user.id)

    #Проверка на маты
    for a in range(0, len(message_text)):
        for i in range(0, len(banworld_list)):
            #Проверяем все слова из сообщения на список матов
            if str(message_text[a]) + "\n" == banworld_list[i]:
                #Если подошёл даем предупреждение
                users[message.from_user.id]["mats"] += 1
                # Если предупреждений много баним
                if users[message.from_user.id]["mats"] >= MAX_MATS:
                    users[message.from_user.id]["is_ban"] = True
                    await bot.ban_chat_member(message.chat.id, message.from_user.id)
                #Пишем что выдали предупреждение
                await message.answer(f"Я выдаю предуприждение пользователю {message.from_user.first_name}\nЧисло предупреждений: {users[message.from_user.id]['mats']}")
                await message.delete()
                break


banworld.close()

dp.run_polling(bot)







>>>>>>> 8833888 (StatProject!)
