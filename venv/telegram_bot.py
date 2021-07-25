from secret_token import TOKEN
from aiogram import *
import logging

API_TOKEN = TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help', 'just somthing info'])
async def send_welcome(message: types.Message):
    """
    This just info for you
    """
    await message.reply('Hi i am EchoBot')


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
