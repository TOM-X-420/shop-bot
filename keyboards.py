# Keyboards for Telegram Bot

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Example inline keyboard layout

def create_start_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    button_a = InlineKeyboardButton('Button A', callback_data='button_a')
    button_b = InlineKeyboardButton('Button B', callback_data='button_b')
    keyboard.add(button_a, button_b)
    return keyboard

# Additional keyboard layouts can be added here.