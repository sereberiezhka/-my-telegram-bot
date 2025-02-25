import asyncio
import logging
import sys
from os import getenv

import os

print("🔄 Загружаю переменные окружения...")
TOKEN = os.getenv("TOKEN")

if not TOKEN:
    print("❌ Ошибка: Railway НЕ передает TOKEN!")
else:
    print(f"✅ Railway передает TOKEN: {TOKEN[:10]}...")
    
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Bot token can be obtained via https://t.me/BotFather

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Тестовый запуск бота")

@dp.message(Command('site'))
async def command_site_handler(message: Message) -> None:
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton( 
                    text="Перейти в Магазин",
                    web_app=WebAppInfo(url=f'https://ms-store54.ru'),
                )
            ]
        ]
    )
    await message.answer ("Нажми на кнопку чтобы перейти в магазин", reply_markup=markup)
    


@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
