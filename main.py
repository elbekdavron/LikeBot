from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import os

votes = {
    "likes": 0, 
    "dislikes": 0
    }

TOKEN = os.getenv("TOKEN")

def start(update, context):

    photo = open("image.jfif", "rb")

    keyboard = [
        [InlineKeyboardButton(f"👍 Like {votes['likes']}", callback_data="like")],
        [InlineKeyboardButton(f"👎  Dislike {votes['dislikes']}", callback_data="dislike")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_photo(photo=photo, reply_markup=reply_markup)
    
def count(update, context):
    
    if update.callback_query.data == "like":
        votes["likes"] += 1
    elif update.callback_query.data == "dislike":
        votes["dislikes"] += 1

    keyboard = [
        [InlineKeyboardButton(f"👍 Like {votes['likes']}", callback_data="like")],
        [InlineKeyboardButton(f"👎 Dislike {votes['dislikes']}", callback_data="dislike")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.callback_query(reply_markup=reply_markup) 


updater = Updater(TOKEN)  
dispatcher = updater.dispatcher


dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CallbackQueryHandler(count))


updater.start_polling()
updater.idle()