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

MEANNESS = [
    'stinky', 'warty', 'lame', 'covered-in-boils', 'a-CLOWN',
    'blander-than-oatmeal', 'the-absolute-worst', 'an-utter-fool',
    'the-least-stealthy-ninja-ever']   


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <head>
      <title> Start here </title>
      </head>
      <body>
      To go to the Hello page,
      <a href="/hello"> Click here </a>
      </body>
    </html>"""


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
        <form action="/process_hello">
          Would you want a compliment or an insult?
          <input type="radio" name="answer" value="insult"> INSULT
          <input type="radio" name="answer" value="compliment"> COMPLIMENT  
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """

@app.route('/process_hello')
def process_hello():
    """Say hello and prompt for user's name."""
    option = ""

    reply = request.args.get("answer")

    if reply == "compliment":
      for compliment in AWESOMENESS:
        option = option + f"<option value={compliment}>{compliment}</option>"

      response = f"""
        <!doctype html>
        <html>
          <head>
            <title>Hi There!</title>
          </head>
          <body>
            <h1>Hi There!</h1>
            <form action="/greet">
              What's your name? <input type="text" name="person">
              What would you want your compliment to be?
              <select name="compliment">
              {option}
              <input type="submit" value="Submit">
            </form>
          </body>
        </html>
        """   

    if reply == "insult":
      for insult in MEANNESS:
        option = option + f"<option value={insult}>{insult}</option>"

      response = f"""
        <!doctype html>
        <html>
          <head>
            <title>Hi There!</title>
          </head>
          <body>
            <h1>Hi There!</h1>
            <form action="/diss">
              What's your name? <input type="text" name="person">
              What would you want your insult to be?
              <select name="insult">
              {option}
              <input type="submit" value="Submit">
            </form>
          </body>
        </html>
        """   

    return response  

@app.route('/greet')
def greet_person():
    """Greet user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

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
def diss_person():
    """Diss user by name."""

    player = request.args.get("person")

    insult = request.args.get("insult")
    print(f"!!!!!!!!!!!!!!{insult}")

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
