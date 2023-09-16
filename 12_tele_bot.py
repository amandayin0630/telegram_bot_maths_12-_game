import os
import telebot
import random
import sympy

API_KEY = "6504782512:AAFuwytXMDoiJwJXz8SS0jltDdWgthsRBSs"  # Replace with your actual API key
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['hi'])
def greet(message):
    bot.reply_to(message, "Hey, I hope you are doing great! Type '/12' to proceed to the game. I will give you 4 random integers ranging from 1 to 13, and you need to type in a math equation using all 4 integers, including +, -, *, /, () to get the result of 12. Type in '/example' for an example.")

@bot.message_handler(commands=['example'])
def example(message):
    bot.send_message(message.chat.id, "Given 2, 4, 8, 1, you may type in: 1*(2*8-4), this would generate 12, making use of all provided integers, which is a correct solution.")

@bot.message_handler(commands=['12'])
def generate_random_numbers(message):
    random_integers = [random.randint(1, 13) for _ in range(4)]
    bot.send_message(message.chat.id, f"Here are your 4 random integers: {', '.join(map(str, random_integers))}")
    bot.send_message(message.chat.id, "Now, try to create a math equation using these numbers to get 12. For example, you can type '/solve 2*4*1-8' to check if it's correct.")

@bot.message_handler(commands=['solve'])
def solve_equation(message):
    try:
        equation = message.text.split(' ', 1)[1]
        random_integers = [random.randint(1, 13) for _ in range(4)]
        result = sympy.sympify(equation).subs({1: random_integers[0], 2: random_integers[1], 4: random_integers[2], 8: random_integers[3]})
        if result == 12:
            bot.send_message(message.chat.id, f"Congratulations! Your equation '{equation}' results in 12.")
        else:
            bot.send_message(message.chat.id, f"Sorry, your equation '{equation}' results in {result}, not 12. Try again!")
    except Exception as e:
        bot.send_message(message.chat.id, f"An error occurred: {str(e)}")

bot.polling()
