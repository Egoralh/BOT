from telebot import *
import random

bot = TeleBot("5387760192:AAFXFOnqs_8-zM9xPqrQG3rrlRNWEaVnfmE")


@bot.message_handler(commands=["hello"])
def sendMessage(mess):
    bot.reply_to(mess, "Привет!")


@bot.message_handler(commands=["ask"])
def askBot(mess):
    bot.reply_to(mess, "Чем могу помочь?")


@bot.message_handler(commands=["support"])
def buttons(message):
    markup = telebot.types.ReplyKeyboardMarkup()
    b1 = telebot.types.KeyboardButton("Завис компьютер")
    markup.add(b1)
    bot.send_message(message.chat.id, "Что случилось?", reply_markup=markup)


@bot.message_handler(commands=["getImage"])
def getImage(mess):
    bot.send_photo(mess.chat.id, photo=open("images/20110527-_MG_6911.jpg", 'rb'))


@bot.message_handler(func=lambda message:True)
def dialog(message):
    if message.text.lower() == "привет":
        readFile(message, "./greeting.txt")
    elif message.text.lower() == "как дела":
        readFile(message, "affairs.txt")
    elif message.text.lower() == "завис компьютер":
        readFile(message, "./computer.txt")
    if message.text.lower() == "еще":
        bot.send_photo(message.chat.id, photo=open("images/20110527-_MG_6911.jpg", 'rb'))


def readFile(message, fileName):
    file = open(fileName, "r", encoding="UTF-8")
    list = file.read().split("\n")
    file.close()
    bot.reply_to(message, random.choices(list))

bot.polling()
