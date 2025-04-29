import asyncio
import keybord
import random
from aiogram import Bot, types, Dispatcher
import logging
from aiogram.enums import ParseMode
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery
import keybord as kb
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from database.models import async_main
from aiogram import F
from data.config import TOKEN


logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN, Parse_Mode=ParseMode.HTML)
dp = Dispatcher()

class Reg(StatesGroup):
    name = State()
    surname = State()
    number_phone = State()
    city = State()
    hobby = State()

@dp.message(Command("start"))
async def reg(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer(f"Приветсвую в нашем боте <b>{message.from_user.full_name}</b>\nПройдем регистрацию\nВведите ваше имя", parse_mode=ParseMode.HTML)

@dp.message(Reg.name)
async def reg_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.surname)
    await message.answer("Введите вашу фамилию")

@dp.message(Reg.surname)
async def reg_surname(message: Message, state: FSMContext):
    await state.update_data(surname=message.text)
    await state.set_state(Reg.number_phone)
    await message.answer("Введите ваш номер телефона начиная с +7")

@dp.message(Reg.number_phone)
async def reg_number(message: Message, state: FSMContext):
    await state.update_data(number_phone=message.text)
    await state.set_state(Reg.city)
    await message.answer("Введите ваш город жительства")

@dp.message(Reg.city)
async def reg_city(message: Message, state: FSMContext):
    await state.update_data(city=message.text)
    await state.set_state(Reg.hobby)
    await message.answer("Введите ваше хобби")

@dp.message(Reg.hobby)
async def reg_hobby(message: Message, state:FSMContext):
    await state.update_data(hobby=message.text)
    data = await state.get_data()
    await message.answer(f"Спасибо за регестрацию\nИмя: {data["name"]}\nФамилия: {data["surname"]}\nНомер телефона: {data["number_phone"]}\nГород: {data["city"]}\nХобби: {data["hobby"]}")
    await state.clear()

@dp.message(Command("help"))
async def message_help(message: types.Message):
    await message.answer("""
   """)

@dp.message(Command("play"))
async def send_welcome(message: types.Message):
    await message.answer("Будешь играть?", reply_markup=kb.main)

@dp.callback_query(F.data == "yes")
async def yes(callback: CallbackQuery):
    await callback.answer("Вы выбрали Играть", show_alert=True)
    await callback.message.edit_text("Во что будешь играть?", replay_markup= kb.game)


@dp.callback_query(F.data == "no")
async def No(callback: CallbackQuery):
    await  callback.message.edit_text("Приходи в следующий раз")

async def main():
    await async_main()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


