
from flask import Flask, render_template,request
import random


app = Flask(__name__)

choices = ["rock", "paper","scissors"]
facts = [
    'rock paper scissors is the oldest hand game in the world',
    'this is a fun and easy hand game that anyone can learn and enjoy',
    'this game is a great way to improve critical thinking and communication skills'
]




if __name__ == '__main__':
            app.run(debug=True)

@app.route('/about')
def about ():
    return render_template('about.html')

@app.route('/game')
def game():
    return render_template('game.html')



@app.route('/result', methods=['POST'])
def result():
    user_choice = request.form['choice']
    computer_choice = random.choice(choices)
    result = play(user_choice, computer_choice)
    return render_template('result.html',user_choice=user_choice, computer_choice=computer_choice, result=result)

@app.route('/')
def index():
    return render_template('index.html', facts=facts)

def play(user_choice, computer_choice):
    if user_choice == computer_choice:
        result = "it's a tie!"
    elif user_choice == "rock" and computer_choice == "scissors":
        result ="you win!"
    elif user_choice == "paper" and computer_choice == "rock":
        result = "you win!"
    elif user_choice == "scissors" and computer_choice == "paper":
        result = "you win!"
    else:
        result = "you lose!"
    return result



























