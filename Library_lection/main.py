from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_comand import *






updater = Updater('5170186164:AAH30zwatyo2ZKdqFnkJMRCtTOPaZVHnX54')

updater.dispatcher.add_handler(CommandHandler('hi', hi_comand))
updater.dispatcher.add_handler(CommandHandler('time', time_comand))
updater.dispatcher.add_handler(CommandHandler('help', help_comand))
updater.dispatcher.add_handler(CommandHandler('sum', sum_comand))
print('server start')
updater.start_polling()
updater.idle()


# import matplotlib.pyplot as plt
# import numpy as np

# list = [2,4,6,3,1]
# plt.plot(list)


# plt.show()


# import emoji

# print(emoji.emojize('Python is :thumbs_up:'))


# from progress.bar import Bar
# import time

# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(0.5)
#     bar.next()
# bar.finish()



# from isOdd import isOdd

# print(isOdd(1)) 
# print(isOdd(5))

# print(isOdd(0)) 
# print(isOdd(4)) 