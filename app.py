from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display message about the user's favorite dessert."""
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def mad_libs(adjective, noun):
    """Display the madlibs based on the inputs"""
    story = f"There is a magical {adjective} {noun} on my grandparents farm. The {adjective} {noun} makes {adjective} colored cheese!"
    return story

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    """Multiply the numbers and return result or error"""
    if number1.isdigit() and number2.isdigit():
        result = int(number1) * int(number2)
        return f'{number1} times {number2} is {result}.'
    else:
        return 'Try again and enter 2 numbers'

@app.route('/sayntimes/<word>/<n>')
def say_n_times(word, n):
    """Repeats a word multiple times and returns the result or an error message."""
    if n.isdigit():
        n = int(n)
        result = ' '.join([word] * n)
        return result
    else:
        return 'Try again by entering a word and a number!'

@app.route('/dicegame')
def dice_game():
    """Rolling a dice and determine win/loss if you get a 6 or less."""
    roll = random.randint(1, 6)
    if roll == 6:
        return f'You rolled a {roll}. You win'
    else:
        return f'You rolled a {roll}. You loose'



if __name__ == '__main__':
    app.run(debug=True, port=5001)

