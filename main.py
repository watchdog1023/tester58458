from telegram.ext import Updater, CommandHandler
import requests
import re
import os

content_array = []
#1228609641:AAEiAwIeyqAByW95S_OxWFITi0JUu9HjyGU tester
#1156004345:AAGYIogVoAMSter7H_RUrQIiJPb_dLVfl_w allfather

def file_read(fname):
    with open(fname) as f:
        for line in f:
            content_array.append(line)

def echo(update, context):
    chat_id = update.message.chat_id
    command = context.args[0].lower()
    print(command)
    os.system("python3 phdler.py custom " + command)


def bop(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id,text="AllFATHER!")
    for root, dirs, files in os.walk("./handpicked"):  
        for filename in files:
            bot.send_video(chat_id=chat_id,video=open("handpicked/" + filename + ".mp4", 'rb'), supports_streaming=True)    

def main():
    file_read('test.txt')
    for i in range(len(content_array)):
        os.system("python3 phdler.py custom " + content_array[i])
    updater = Updater('1228609641:AAEiAwIeyqAByW95S_OxWFITi0JUu9HjyGU',use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('send',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
