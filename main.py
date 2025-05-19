import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router
from aiogram.utils.markdown import hbold
from aiogram.types import FSInputFile

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())
router = Router()
dp.include_router(router)

@router.message(commands=["start"])
async def start(msg: Message):
    await msg.answer("Ня! Я твоя Мия-тян, телеграм-нянька. Готова пинать тебя за лень!")

@router.message(commands=["help"])
async def help_cmd(msg: Message):
    await msg.answer(
        "/start - запуск бота\n"
        "/check - проверить задачи\n"
        "/help - помощь\n"
        "/todo - добавить задачу\n"
        "/tasks - список задач"
    )

@router.message(commands=["todo"])
async def todo_cmd(msg: Message):
    task = msg.text[6:].strip()
    if not task:
        await msg.answer("Напиши задачу после команды, дурында!\nПример: /todo купить протеин")
        return
    with open("tasks.txt", "a", encoding="utf-8") as f:
        f.write(f"- {task}\n")
    await msg.answer("Задача добавлена! 📝")

@router.message(commands=["tasks"])
async def list_tasks(msg: Message):
    if not os.path.exists("tasks.txt"):
        await msg.answer("Задач нет! Ты безответственное чмо! 😤")
        return
    with open("tasks.txt", encoding="utf-8") as f:
        tasks = f.read()
    await msg.answer("Вот твои задачи:\n" + tasks)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
