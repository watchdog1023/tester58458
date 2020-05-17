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
    update.message.replay(text="AllFATHER!")
    update.message.reply_video(video=open('handpicked/*.mp4', 'rb'), supports_streaming=True)    

def main():
    updater = Updater('1228609641:AAEiAwIeyqAByW95S_OxWFITi0JUu9HjyGU',use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('hi',echo))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
