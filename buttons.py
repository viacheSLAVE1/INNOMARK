from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='статистика')]
    ],    resize_keyboard=True)

'''back = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Обратно")]
],resize_keyboard=True,input_field_placeholder='выбирите пункт меню')'''
'''prof = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Зарегистрироваться')], [KeyboardButton(text='Обратно')]
],resize_keyboard=True,
                input_field_placeholder='выбирите пункт меню'
)'''

'''profenter = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='статистика')], [KeyboardButton(text='Обратно')]
],resize_keyboard=True,
                input_field_placeholder='выбирите пункт меню'
)'''

'''reg = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='да')], [KeyboardButton(text='Обратно')]
],resize_keyboard=True,
input_field_placeholder='выбирите пункт меню'
)'''

