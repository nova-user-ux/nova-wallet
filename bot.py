import os
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo,
)

TOKEN = os.getenv("BOT_TOKEN")

WEB_APP_URL = "https://nova-user-ux.github.io/nova-wallet/"

dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message):
    text = """🚀 Добро пожаловать в NOVA Wallet!

Твоя цифровая экосистема в одном месте.

💬 Messenger
🛍 Marketplace
🎁 Gifts
⭐ Stars
💎 Digital Collectibles
💰 Wallet"""

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🚀 Play",
                    web_app=WebAppInfo(url=WEB_APP_URL)
                )
            ]
        ]
    )

    await message.answer(
        text,
        reply_markup=keyboard
    )


async def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN is not set")

    bot = Bot(TOKEN)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
