"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]

player = ""


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """Display madlib game."""

    # Get player's decision on whether to play
    will_play = request.args.get("play")

    if will_play == "no":
        # If player chose no, then load a goodbye page
        return render_template("goodbye.html")
    elif will_play == "yes":
        # Otherwise, player chose yes, and load the game page.
        return render_template("game.html")


@app.route('/madlib')
def show_madlib():
    """Display madlib result."""

    # Get player's madlib inputs
    chara = request.args.get("character").title()
    color = request.args.get("color")
    noun = request.args.get("noun")
    adj = request.args.get("adjective")

    if adj[0] in ('a', 'e', 'i', 'o', 'u'):
        adj = f"an {adj}"
    else:
        adj = f"a {adj}"

    return render_template("madlib.html",
                            character=chara,
                            color=color,
                            noun=noun,
                            adjective=adj)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
