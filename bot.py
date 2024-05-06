import asyncio
import logging
import sys

from api_token import API_TOKEN_BOT
from app import convert,log_request
from aiogram import Bot, Dispatcher,F
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties
from aiogram.types import Message
from aiogram.filters import CommandStart


bot = Bot(API_TOKEN_BOT, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# @bot.message_handler(content_types=["text"])
# def repeat_all_messages(message): # Название функции не играет никакой роли
#     answer = convert(message.text)
#     print(message.chat.id, message.text, answer, sep=' -- ')
#     log_request(message.chat.id, message.text, answer)
#     bot.send_message(message.chat.id, str(answer).replace("'", '"'))


@dp.message(CommandStart())
async def start_command(message: Message):
    await message.answer(text="ok")



@dp.message(F.text)
async def send_echo(message: Message):
    answer = convert(message.text)
    print(message.chat.id, message.text, answer, sep=' -- ')
    log_request(message.chat.id, message.text, answer)
    await message.reply(text=str(answer).replace("'", '"'))

async def main() -> None:


    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())