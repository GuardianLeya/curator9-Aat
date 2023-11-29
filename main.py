import telebot

bot = telebot.TeleBot('6926495370:AAG3OwZjrjxjoOUFj4FzSt2xlj1QY_F5vi8')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Здравствуй, путещественник. Что желаете?', parse_mode='Markdown')


@bot.message_handler(commands=['tea'])
def main(message):
    bot.send_message(message.chat.id, 'Вот ваш восхитительный чай', parse_mode='Markdown')


@bot.message_handler(commands=['alcohol'])
def main(message):
    bot.send_message(message.chat.id,
                     'Вот ваш восхитительный напиток! Но будьте осторожны, не пейте слишком много, иначе _кто знает что может случиться_.',
                     parse_mode='Markdown')


@bot.message_handler(commands=['chill'])
def main(message):
    bot.send_message(message.chat.id,
                     'Хорошо. Можете подняться на верхние этажи. У нас там конаты отдыха. *Приятного вечера!*',
                     parse_mode='Markdown')


bot.infinity_polling()
