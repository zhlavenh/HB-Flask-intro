"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']
INSULTS = ['stupid', 'disappointing', 'a gargoyle', 'so bad if Mr.Rogers was your neighbor, he\'d move',
    'so ugly France called and said can we give their gargoyle back', 
    'not pretty enough to get away with being that stupid.', 'no trial and all error'
]

Pages = [
    '/greet', '/diss'
]


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
    Hi! This is the home page.<br>
    <body>
    <a href="/hello">Go to hello page</a>
    </body>
    </html>
    
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action={choice(Pages)}>
          What's your name? <input type="text" name="person"><br><br>

          <select name="compliments">
            <option value"">Please choose an option</option>
            <option value="cool">Cool!</option>
            <option value="sweet">Sweet!</option>
          </select><br>

            <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliments")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """

@app.route('/diss')
def insult_person():
        
      player = request.args.get("person")

      insult = choice(INSULTS)

      return f"""
      <!doctype html>
      <html>
        <head>
          <title>An Insult</title>
        </head>
        <body>
          Hi, {player}! I think you're {insult}!
        </body>
      </html>
      """

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
