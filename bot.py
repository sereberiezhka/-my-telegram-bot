import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = "8064051318:AAFsTBfv-fjbNe4mJA81d2T2TAGM9QYGFwY"  # Твой токен от BotFather

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
