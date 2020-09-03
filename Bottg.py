import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputFile
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

API_TOKEN = '1360084291:AAGK78QN_bx8FzlpqMKRyV-xvVTpW3FqzAo'

logging.basicConfig(level = logging.INFO)

bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot)

opt = {
    'fub': ('Привет', 'привет','Привет!','привет!', 'Hi', 'hi')
}

@dp.message_handler(commands='start')
async def send_welcom(message: types.Message):
    await message.answer('Привет, я бот!')

@dp.message_handler()
async def echo(message: types.Message):
    print(message.text)
    if message.text in (opt['fub']):
        await message.answer("Привет!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)
