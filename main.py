
import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(msg: Message):
    await msg.answer("Ня! Я твоя Мия-тян, телеграм-нянька. Готова пинать тебя за лень!")

@dp.message_handler(commands=["help"])
async def help_cmd(msg: Message):
    await msg.answer("/start — запуск бота\n/check — проверить задачи\n/help — помощь")
/help — помощь
/todo — добавить задачу")

@dp.message_handler(commands=["todo"])
async def todo_cmd(msg: Message):
    task = msg.get_args()
    if not task:
        await msg.answer("Напиши задачу после команды, дурында!
Пример: /todo купить протеин")
        return
    with open("tasks.txt", "a", encoding="utf-8") as f:
        f.write(f"- {task}\n")
    await msg.answer("Задача добавлена!")

@dp.message_handler(commands=["tasks"])
async def list_tasks(msg: Message):
    if not os.path.exists("tasks.txt"):
        await msg.answer("Задач нет! Ты безответственное чмо!")
        return
    with open("tasks.txt", encoding="utf-8") as f:
        tasks = f.read()
    await msg.answer("Вот твои задачи:
" + tasks)

if __name__ == "__main__":
    executor.start_polling(dp)
