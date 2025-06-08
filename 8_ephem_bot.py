"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import datetime #импорт обработки даты (стандартный модуль питона)
from datetime import date
import ephem #импорт астрономического модуля (устанавливается отдельно)

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def planet_cons(update, context):
    current_date = date.today()
    print(current_date)
    message_text = update.message.text
    parts = message_text.split()
    if len(parts) > 1:
        planet = parts[1]
        if planet.lower() == 'mars':
            planet_constellation = ephem.Mars(current_date)
            print(ephem.constellation(planet_constellation))
        elif planet.lower() == 'venus':
            planet_constellation = ephem.Venus(current_date)
            print(ephem.constellation(planet_constellation))
        elif planet.lower() == 'mercury':
            planet_constellation = ephem.Mercury(current_date)
            print(ephem.constellation(planet_constellation))
        elif planet.lower() == 'jupiter':
            planet_constellation = ephem.Jupiter(current_date)
            print(ephem.constellation(planet_constellation))
        elif planet.lower() == 'saturn':
            planet_constellation = ephem.Saturn(current_date)
            print(ephem.constellation(planet_constellation))
        else:
            print('Мой создатель слишком ленив чтобы добавить остальные планеты')
    else:
        print('Планету то мне не назвали')


def main():
    mybot = Updater("КЛЮЧ, КОТОРЫЙ НАМ ВЫДАЛ BotFather", request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_cons))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
