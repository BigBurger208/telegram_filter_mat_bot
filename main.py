from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

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
    await message.answer("Hay! Go to game!")

@dp.message(Command(commands=["help"]))
async def help_command(message: Message):
    await message.answer("Hey! You ara a idiot")

@dp.message(Command(commands=["score"]))
async def start_commands(message: Message):
    await message.answer(f'Всего игр сыгранно: {user["total_game"]} \n'
                         f'Выйгранных игр: {user["win"]}')
                         
    

if __name__ == "__main__":
    dp.run_polling(bot)