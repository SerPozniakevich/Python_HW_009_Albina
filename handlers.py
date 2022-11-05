
from aiogram import types
import emoji
from datetime import datetime
from time import time


async def hi(message: types.Message):
    await message.answer(f'Приветули, {message.from_user.full_name}')
    await message.answer(emoji.emojize(':thumbs_up:'))


async def time(message: types.Message):
    await message.answer(f'{datetime.now().strftime("%d.%m.%Y. %H:%M")}')


async def help(message: types.Message):
    await message.answer(f'/hi - команда для приветствия\n/time - команда для получения актуальных даты и времени\n\
/help - команда меню бота\nКоманды калькулятора.\nНапишите команду необходимого действия и два числа через пробел.\n\
Например:( /sum 22 33 ) В ответ получите: ( 22 + 33 = 55)\n/sum - команда сложения\n\
/sub - команда вычитания\n/multi - команда умножения\n/div - команда деления')


async def sum(message: types.Message):
    msg = message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await message.answer(f'{x} + {y} = {x + y}')


async def multi(message: types.Message):
    msg = message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await message.answer(f'{x} * {y} = {x * y}')


async def div(message: types.Message):
    msg = message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await message.answer(f'{x} / {y} = {x / y}')


async def sub(message: types.Message):
    msg = message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await message.answer(f'{x} - {y} = {x - y}')

