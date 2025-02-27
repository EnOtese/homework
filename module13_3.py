from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
import asyncio

API = "API"
bot = Bot(token=API)
dp = Dispatcher(storage=MemoryStorage())


@dp.message(Command("start"))
async def start(message: types.Message):
    print(f"{message.from_user.username} запустил бота")
    await message.answer(text='Привет! Я бот помогающий твоему здоровью.')


@dp.message(lambda message: message.text == "Urban")
async def urban_message(message):
    print("Urban message")


@dp.message()
async def all_message(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.')
    print(f"Мы получили сообщение! Вот оно: {message.text} \n ^ от {message.from_user.username}")


if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
