from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')
PROXY = {'proxy_url': 'socks5://5.178.61.121:9999'}
    # ,'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}



def greet_user(bot, update):
    text = 'Called/start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    tg_token = '378879267:AAFQr6zC8glce5A8QPQOpiKLwcjBoe2-lXA'
    tg_bot = '@YaGo_Context_bot'
    
    mybot = Updater(tg_token, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

main()    