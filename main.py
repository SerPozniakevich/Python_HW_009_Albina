from aiogram import Bot, Dispatcher, executor
import handlers

API_TOKEN = 'Token'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

dp.register_message_handler(handlers.hi, commands=["hi"])
dp.register_message_handler(handlers.time, commands=["time"])
dp.register_message_handler(handlers.help, commands=["help"])
dp.register_message_handler(handlers.sum, commands=["sum"])
dp.register_message_handler(handlers.multi, commands=["multi"])
dp.register_message_handler(handlers.div, commands=["div"])
dp.register_message_handler(handlers.sub, commands=["sub"])

if __name__ == '__main__':

    print('Бот включён')
    executor.start_polling(dp, skip_updates=True) # пропуск команд отправленных до старта бота
    print('Бот выключен')