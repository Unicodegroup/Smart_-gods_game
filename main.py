import os
from dotenv import load_dotenv
import telebot

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

if not API_TOKEN:
    raise ValueError("API_TOKEN is not set. Check your .env file.")

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Hi there, welcome to the game!")




bot.infinity_polling()