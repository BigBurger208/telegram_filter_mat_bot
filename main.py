from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram import F

import random

BOT_TOKEN = "7202593170:AAExJYXkm_2PzQnT1POLLzfhpXBruvw1N4U"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

ATTEMPTS = 5

user = {
    "in_game": False,
    "secret_number": None,
    "attemps": None,
    "total_game": 0,
    "win": 0
}

def random_number() -> int:
    return random.randint(0, 100)


@dp.message(CommandStart())
async def start_command(message: Message):
    await message.answer("Начнем играть?")

@dp.message(Command(commands=["help"]))
async def help_command(message: Message):
    await message.answer("Вы должны угадать какое число я загадал от 1 до 100")

@dp.message(Command(commands=["score"]))
async def start_commands(message: Message):
    await message.answer(f'Всего игр сыгранно: {user["total_game"]} \n'
                         f'Выйгранных игр: {user["win"]}')

@dp.message(Command(commands=["cancel"]))
async def cancel_command(message: Message):
    if user["in_game"] == True:
        user["in_game"] = False
        await message.answer("Вы вышли из игры")
    else:
        await message.answer("Мы с вами не играем")


@dp.message(F.text.lower().in_(["да", "давай", "го", "согласен", "начнем"]))
async def start_game(message: Message):
    if not user["in_game"]:
        user["in_game"] = True
        user["secret_number"] = random_number()
        user['attemps'] = ATTEMPTS
        await message.answer("Игра начинается я загадал число от 1 до 100")
    else:
        await message.answer("Мы пока играем если хотите закончить напишите /cancel")

@dp.message(F.text.lower().in_(["нет", "не хочу", "не"]))
async def not_start_game(message: Message):
    if not user["in_game"]:
        await message.answer("Жаль но ладно")
    else:
        await message.answer("Мы сейчас играем")

@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def game(message: Message):
    if user["in_game"]:
        if int(message.text) == user["secret_number"]:
            user["in_game"] = False
            user["total_game"] += 1
            user["win"] += 1
            await message.answer("You Win!")
        elif int(message.text) > user["secret_number"]:
            user['attemps'] -= 1
            await message.answer("Мое чило меньше")
        elif int(message.text) < user["secret_number"]:
            user['attemps'] -= 1
            await message.answer("Мое чило больше")

        if user["attemps"] == 0:
            user["in_game"] = False
            user["total_game"] += 1
            await message.answer("You Lose!")
    else:
        await message.answer("Мы еще не играем")



@dp.message()
async def message_our(message: Message):
    if user["in_game"]:
        await message.answer("Мы сейчас играем пришите числа")
    else:
        await message.answer("Если хотите сыграть напишите Да")

if __name__ == "__main__":
    dp.run_polling(bot)