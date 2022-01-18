#!/usr/bin/python3

from telegram import *
from telegram.ext import *
import snap7
import sh
# from requests import *

updater = Updater(token="2115883750:AAGqskwSwvRD8iQlFA8vn9rUKG7DY8qM-jg")
dispatcher = updater.dispatcher

text_laguntza = "/laguntza"
text_piztu = "/piztu"
text_itzali = "/itzali"
text_konektatu = "/konektatu"

client = None

def startCommand(update: Update, context: CallbackContext):
    buttons = [[KeyboardButton(text_laguntza),KeyboardButton(text_konektatu)]
               ,[KeyboardButton(text_piztu),KeyboardButton(text_itzali)]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Ongi etorri bot honetara, eman /laguntza akzioak ikusteko", reply_markup=ReplyKeyboardMarkup(buttons))


def laguntza(update: Update, context: CallbackContext):
    update.message.reply_text("""Botoietako aukerak :-
    /konektatu - PLCra konektatu
    /piztu - irteerak 1era jartzeko
    /itzali - irteerak 0era itzaltzeko""")

def connect(update: Update, context: CallbackContext):
    global client
    client = snap7.client.Client()
#    for num in range(255):
#        ip = "192.168.0."+str(num)

#        try:
#            sh.ping(ip, "-c 1",_out="/dev/null")
#            update.message.reply_text("PING ",ip , "OK, saiatu konektatzen")
#            client.connect(ip)
#            if client.get_connected():
#                continue
#        except sh.ErrorReturnCode_1:
#            print("PING ", ip, "FAILED")
    ip = "192.168.0.1"
    client.connect(ip,0,1)
    if client.get_connected():
        update.message.reply_text("PLCra konektatuta")

def piztu(update: Update, context: CallbackContext):
    global client
    salidas = b'\xFF'
    client.ab_write(0, salidas)
    update.message.reply_text("Piztu dira")


def itzali(update: Update, context: CallbackContext):
    global client
    salidas = b'\x00'
    client.ab_write(0, salidas)
    update.message.reply_text("Itzali dira")


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)


dispatcher.add_handler(CommandHandler("start", startCommand))
updater.dispatcher.add_handler(CommandHandler('konektatu', connect))
updater.dispatcher.add_handler(CommandHandler('piztu', piztu))
updater.dispatcher.add_handler(CommandHandler('laguntza', laguntza))
updater.dispatcher.add_handler(CommandHandler('itzali', itzali))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown_text))  # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
