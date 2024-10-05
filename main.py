# -*- coding: utf-8 -*-
import telebot
import random

#список фраз
compliments = ["I really admire how you are handling this. I know it’s difficult.", "Take care.", "Stay well", "I care.", "It’s Okay to feel this way.", "It’s Okay to feel this way.", "You aren’t weak.", "How can console you or cheer you up?", "Hang in there ", "Don’t give up", "Keep fighting!", "Stay strong", "Go for it", "It’s worth a shot", "I’ll support you either way", "I’m behind you 100%", "It’s totally up to you", "I’m so proud of you! ", "Keep up the good work", "Believe in yourself.", "Lighten up", "it your best shot", "Fortune favours the bold", "You're on the right track", "sky’s the limit", "When the going gets tough, the tough get going", "Where there's a will there's a way", "There’s light at the end of the tunnel", "If at first you don't succeed... try and try again", " Every dog has its"]

#список фото
pngs = (r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\котики\1.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\котики\2.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\котики\3.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\котики\4.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\котики\5.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\котики\6.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\котики\7.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\котики\8.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\котики\9.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\котики\10.png", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\котики\11.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\котики\12.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\котики\13.png", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\котики\14.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\котики\15.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\котики\16.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\котики\17.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\котики\18.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\котики\19.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\котики\20.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\котики\21.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\котики\22.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\котики\23.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\котики\24.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\котики\25.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\котики\26.png", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\котики\27.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\котики\28.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\котики\29.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\котики\30.jpg")
#
jpg = [r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\1.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\2.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\3.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\4.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\5.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\6.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\7.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\8.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\9.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\10.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\11.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\12.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\13.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\14.png", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\15.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\16.png", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\17.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\18.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\19.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\20.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\21.png", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\22.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\23.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\24.png", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\25.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\26.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\27.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\28.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\29.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\30.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\31.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\32.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\33.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\34.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\35.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\36.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\37.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\38.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\39.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\40.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\41.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\42.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\43.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\44.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\45.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\46.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\47.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\48.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\49.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\50.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\51.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\52.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\53.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\54.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\55.png", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\56.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\57.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\58.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\59.jpg", r"C:\Users\Пользователь\Desktop\IT 2023\котик ботик\кт\60.png"]

#создание объекта бота
token='6618755336:AAFJCm5VYfNH4vs1H6QmmNBQkbBjvu9HG2c'
bot=telebot.TeleBot(token)


#команда старт
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет, мяу")

#реакция на сообщение пользователя
@bot.message_handler()
def info(message):
  #ответ пизда
  if message.text.lower() == "да":
      bot.send_message(message.chat.id,"пизда")
  #присылает фото или фразу
  else:
      number = random.randint(1, len(compliments)-1)
      #фраза
      if(number % 2 == 0):
        bot.send_message(message.chat.id,compliments[number])
        #фото
        number_ind1 = random.randint(0, len(jpg)-1)
        photo_kitten  = open(jpg[number_ind1] , 'rb')
        bot.send_photo(message.chat.id, photo = photo_kitten)
      #фото
      else:
          number_ind = random.randint(0, len(compliments)-1)
          photo_cat  = open(pngs[number_ind-1], 'rb')
          bot.send_photo(message.chat.id, photo = photo_cat)


bot.infinity_polling()
