from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spy import *

def hi_comand(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}')

def help_comand(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Привет! Я маленький бот. Я еще мало что умею, например эти команды:\n Для приветствия просто введи: /hi\n Может желаешь узнать точное время, тогда введи: /time \n Я могу складывать два числа, их введи через пробел после команды, например: /sum 123 123 \n А чтоб узнать что я умею пиши: /help)')

def time_comand(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'{datetime.datetime.now().time()}')

def sum_comand(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x + y}')