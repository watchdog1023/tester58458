from telegram.ext import Updater, CommandHandler
import requests
import re
import os

#1228609641:AAEiAwIeyqAByW95S_OxWFITi0JUu9HjyGU tester
#1156004345:AAGYIogVoAMSter7H_RUrQIiJPb_dLVfl_w allfather

def echo(update, context):
    chat_id = update.message.chat_id
    command = context.args[0].lower()
    print(command)
    os.system("python3 phdler.py custom " + command)
    update.message.chat_id.send_message(chat_id=chat_id,text="AllFATHER!")
    bot.send_video(chat_id=chat_id,video=open('handpicked/*.mp4', 'rb'), supports_streaming=True)    


def bop(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id,text="AllFATHER!")
    bot.send_video(chat_id=chat_id,video=open('handpicked/*.mp4', 'rb'), supports_streaming=True)    

def main():
    updater = Updater('1228609641:AAEiAwIeyqAByW95S_OxWFITi0JUu9HjyGU',use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('hi',echo))
    dp.add_handler(CommandHandler('send',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
