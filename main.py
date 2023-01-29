from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters,CallbackQueryHandler
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
import os
from tinydb import TinyDB, table

Token=os.environ['Token']

weather_api=os.environ['api']

# this url get 5 days weather data
db=TinyDB('db.json')
db=db.table('Users')
#
def start(update: Update, context: CallbackContext):
    bot=context.bot
    chat_id=update.message.chat.id 
    text='Assalomu alaykum\nbu bot orqali ob-havo haqida malumot olishinggiz mumkin. Kategoriyalardan birini tanlang.'
    button=ReplyKeyboardMarkup(
        [['Joylashuv bo\'yicha','Shaharlar kesimida'],['Bot haqida']]
    )
    db=TinyDB('db.json')
    table1=db.table('Users')
    if not(table1.contains(doc_id=chat_id)):
        db.insert(table.Document({'tanlov':''},doc_id=chat_id))

    db.insert_multiple([])
    bot.sendMessage(
        chat_id,
        text,
        reply_markup=button
    )

def tanlov(update: Update, context: CallbackContext):
    bot=context.bot 
    chat_id=update.message.chat.id 
    button1=InlineKeyboardButton(text='Ertangi',callback_data='tan ertangi')
    button2=InlineKeyboardButton(text='5 kunlik',callback_data='tan 5_kun')
    button3=InlineKeyboardButton(text='Hozirgi',callback_data='tan hozir')
    button=InlineKeyboardMarkup(
        [[button1,button2],[button3]]
    )
    bot.sendMessage(chat_id,'O\'zingizga kerak ob-havo malumot turini tanlang:',reply_markup=button)


updater = Updater(token=Token)

updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Joylashuv bo\'yicha') | Filters.text('Shaharlar kesimida'),tanlov))


updater.start_polling()
updater.idle()