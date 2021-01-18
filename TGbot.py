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
    elif message.text.lower() == 'вань':
        bot.send_message(message.chat.id, 'Воробьев')
    elif message.text.lower() == 'ваня':
        bot.send_message(message.chat.id, 'Воробьев')
    elif message.text.lower() == 'иван':
        bot.send_message(message.chat.id, 'Воробьев')
    elif message.text.lower() == 'эмиль':
        bot.send_message(message.chat.id, 'Харасов')
    elif message.text.lower() == 'эмль':
        bot.send_message(message.chat.id, 'Харасов')
    elif message.text.lower() == 'евгений':
        bot.send_message(message.chat.id, 'Просто Жека')
    elif message.text.lower() == 'понял':
        bot.send_message(message.chat.id, 'подтверждаю.')
    elif message.text.lower() == 'понел':
        bot.send_message(message.chat.id, 'подтверждаю.')
bot.polling()
