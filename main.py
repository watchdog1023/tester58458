from telegram.ext import Updater, CommandHandler
import requests
import re

#1228609641:AAEiAwIeyqAByW95S_OxWFITi0JUu9HjyGU

def bop(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id,text="AllFATHER!")
    bot.send_video(chat_id=chat_id,video=open('test.mp4', 'rb'), supports_streaming=True)

def main():
    updater = Updater('1156004345:AAGYIogVoAMSter7H_RUrQIiJPb_dLVfl_w')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('hi',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
