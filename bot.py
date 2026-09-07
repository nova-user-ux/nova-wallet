import asyncio
import os

from aiogram import Bot, Dispatcher, Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "🚀 <b>Добро пожаловать в NOVA Wallet!</b>\n\n"
        "Твоя цифровая экосистема в одном месте.\n\n"
        "💬 Messenger\n"
        "🛍 Marketplace\n"
        "🎁 Gifts\n"
        "⭐ Stars\n"
        "💎 Digital Collectibles\n"
        "💰 Wallet",
        parse_mode="HTML",
    )


async def main():
    token = os.getenv("BOT_TOKEN")

    if not token:
        raise RuntimeError("Не задан BOT_TOKEN")

    bot = Bot(token=token)

    dp = Dispatcher()
    dp.include_router(router)

    print("NOVA Bot запущен")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
