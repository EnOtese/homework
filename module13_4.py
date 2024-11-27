from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup, StateFilter
import asyncio

API = "API"
bot = Bot(token=API)
dp = Dispatcher(storage=MemoryStorage())

users = set()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message(Command("start"))
async def start(message: types.Message):
    print(f"{message.from_user.username} запустил бота")
    if message.from_user.id not in users:
        users.add(message.from_user.id)
        print(users)
    await message.answer(text='Привет! Я бот помогающий твоему здоровью.')


@dp.message(Command("Calories"))
async def set_age(message: types.Message, state: FSMContext):
    await message.reply(text='Введите свой возраст:')
    await state.set_state(UserState.age)


@dp.message(StateFilter(UserState.age))
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer(text='Введите свой рост:')
    await state.set_state(UserState.growth)


@dp.message(StateFilter(UserState.growth))
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer(text='Введите свой вес:')
    await state.set_state(UserState.weight)


@dp.message(StateFilter(UserState.weight))
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data['age'])
    growth = float(data['growth'])
    weight = float(data['weight'])
    calories = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.answer(text=f"Ваша норма калорий: {calories}")


@dp.message()
async def all_message(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.')
    print(f"Мы получили сообщение! Вот оно: {message.text} \n ^ от {message.from_user.username}")


if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
