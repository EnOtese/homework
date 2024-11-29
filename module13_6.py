# aiogram 3.15.0
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup, StateFilter
from aiogram.utils.keyboard import KeyboardButton, ReplyKeyboardBuilder, InlineKeyboardButton, InlineKeyboardBuilder
import asyncio

# aiogram 3.15.0
API = "API"
bot = Bot(token=API)
dp = Dispatcher(storage=MemoryStorage())
kb = ReplyKeyboardBuilder()
button = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
kb.row(button, button2)
ikb = InlineKeyboardBuilder()
ibutton = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
ibutton2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
ikb.add(ibutton, ibutton2)

users = set()


# aiogram 3.15.0
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message(lambda message: message.text == "Информация")
async def info(message: types.Message):
    print(f'{message.from_user.username} запросил информацию о боте.')
    await message.answer(text='Это типа информация о боте и всё такое.')


@dp.message(Command("start"))
async def start(message: types.Message):
    print(f"{message.from_user.username} запустил бота")
    if message.from_user.id not in users:
        users.add(message.from_user.id)
        print(f'Записан новый ID: {users}')
    await message.answer(text='Привет! Я бот помогающий твоему здоровью.',
                         reply_markup=kb.as_markup(resize_keyboard=True))


@dp.message(lambda message: message.text == "Рассчитать")
async def main_menu(message):
    await message.answer(text='Выберите опцию:', reply_markup=ikb.as_markup(resize_keyboard=True))


@dp.callback_query(lambda call: call.data == 'formulas')
async def get_formulas(call):
    await call.message.answer(text='(10 х вес в кг) + (6,25 х рост в см) – (5 х возраст в г) + 5')


@dp.callback_query(lambda call: call.data == "calories")
async def set_age(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer(text='Введите свой возраст:')
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

# aiogram 3.15.0
