import telebot

bot = telebot.TeleBot('1250764561:AAH04Jx6rh5OFYcLofdLN9ne52QRdm6RafA')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'Вань':
        bot.send_message(message.chat.id, 'Воробьев')
    elif message.text.lower() == 'Ваня':
        bot.send_message(message.chat.id, 'Воробьев')
    elif message.text.lower() == 'Иван':
        bot.send_message(message.chat.id, 'Воробьев')
    elif message.text.lower() == 'Эмиль':
        bot.send_message(message.chat.id, 'Харасов')
    elif message.text.lower() == 'Эмль':
        bot.send_message(message.chat.id, 'Харасов')
    elif message.text.lower() == 'Евгений':
        bot.send_message(message.chat.id, 'Просто Жека')
bot.polling()
