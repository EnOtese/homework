from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
import asyncio

API = "7587258859:AAFepShzZ0ZleictvfZW4dBHJgvbqha4PtY"
bot = Bot(token=API)
dp = Dispatcher(storage=MemoryStorage())


@dp.message(Command("start"))
async def start(message: types.Message):
    print(f"{message.from_user.username} запустил бота")
    print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer(text='Привет! Я бот помогающий твоему здоровью.')


@dp.message(lambda message: message == "Urban")
async def urban_message(message):
    print("Urban message")


@dp.message()
async def all_message(message: types.Message):
    print('Введите команду /start, чтобы начать общение.')
    print(f"Мы получили сообщение! Вот оно: {message.text} \n ^ от {message.from_user.username}")


if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
