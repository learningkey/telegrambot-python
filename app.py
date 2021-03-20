from telegram import *
from telegram.ext import *

bot_token = "1170703315:AAHljVvPzXCTeUtfHK9gpYTAt8un_VNAAU0"

bot = Bot(bot_token)
print(bot.getMe())


def myfun1(update: Updater, context: CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="My video 1: https://www.youtube.com/watch?v=yvKGaSamadU"
    )


def myfun2(update: Updater, context: CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="My video 2: https://www.youtube.com/watch?v=mGa92NJnX6s&t=58s"
    )


def message_handler(update: Updater, context: CallbackContext):
    chat_id = update.message.chat_id
    text = update.message.text
    bot.send_message(
        chat_id=chat_id,
        text=text,
        parse_mode=ParseMode.HTML
    )


updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('command1', myfun1))
dispatcher.add_handler(CommandHandler('command2', myfun2))
dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
updater.start_polling()
updater.idle()
