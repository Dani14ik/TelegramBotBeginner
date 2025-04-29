from aiogram.types import (KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup)
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

game = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Игральные кости", callback_data="dice")],
    [InlineKeyboardButton(text="Боулинг", callback_data="bowl"), InlineKeyboardButton(text="Слоты", callback_data="slot")],
    [InlineKeyboardButton(text="Баскетбол", callback_data="basket"), InlineKeyboardButton(text="Футбол", callback_data="footb")]
])


main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Да", callback_data="yes")],
    [InlineKeyboardButton(text="Нет",callback_data="no")]
])

games = ["dice", "slot", "bowl", "fottb", "basket"]
async def game():
    keybord = InlineKeyboardBuilder()
    for i in games:
        keybord.add(InlineKeyboardButton(text=i, callback_data=f"i_{i}"))
    return keybord.as_markup()


game = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Игральные кости", callback_data="dice")],
    [InlineKeyboardButton(text="Боулинг", callback_data="bowl"), InlineKeyboardButton(text="Слоты", callback_data="slot")],
    [InlineKeyboardButton(text="Баскетбол", callback_data="basket"), InlineKeyboardButton(text="Футбол", callback_data="footb")]
])