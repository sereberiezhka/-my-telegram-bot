import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = "8092613164:AAFl8KoICDMZK0YDo4XWKIVVlqNSqh4HEV4"  # Твой токен от BotFather

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
