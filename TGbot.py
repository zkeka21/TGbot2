import telebot

bot = telebot.TeleBot('1250764561:AAH04Jx6rh5OFYcLofdLN9ne52QRdm6RafA')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'ок':
        bot.send_message(message.chat.id, 'ок')
    elif message.text.lower() == 'Ок':
        bot.send_message(message.chat.id, 'ОК')
    elif message.text.lower() == 'ok':
        bot.send_message(message.chat.id, 'ok')
    elif message.text.lower() == 'oк':
        bot.send_message(message.chat.id, 'ok')
    elif message.text.lower() == 'оk':
        bot.send_message(message.chat.id, 'ok'  )
    elif message.text.lower() == '0k':
        bot.send_message(message.chat.id, 'ok')
    elif message.text.lower() == '0к':
        bot.send_message(message.chat.id, 'ok')
    elif message.text.lower() == 'Вань':
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