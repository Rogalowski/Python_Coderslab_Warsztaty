from flask import Flask, request

app = Flask(__name__)

html_start = """
    <!DOCTYPE html>
    <html lang="en"> 

    <head>
    <meta charset="UTF-8">
    <title>Guess The Number</title>
    </head>

        <body>
        <h3>Lets Start The Game</h3>
        
            <form  action = "" method = "POST">
            Mini: <input type="text" name="min" value="{}"><br>
            Maxi: <input type="hidden" name = "max" value="{}"> <br>
            <input type="submit" value="OK">
            </form >
            
        </body>
    </html>
    """

HTML_GAME = """
    <!DOCTYPE html>
    <html lang="en"> 

    <head>
    <meta charset="UTF-8">
    <title>Guess The Number</title>
    </head>

        <body>
            <p> Here: {guess} </p>
            <h3>GAME to guess Imagine number 1 - 1000 </h3>
            <p> Turn number: {counter}</p>
            <form  action = "" method = "POST">
            Mini: <input type="text"  name = "min" value="{min}"> <br>
            Maxi: <input type="text"  name = "max" value="{max}"> <br>
            Guess:<input type="text" name = "guess" value="{guess}"> <br>
            Counter: <input type="text" name = "counter" value="{counter}"> <br>

            <br>

            <input type="submit" name="answer" value="Too Big">
            <input type="submit" name="answer" value="Too Small">
            <input type="submit" name="answer" value="Correct">
            </form >
        </body>
    </html>
    """
html_win = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Guess The Number</title>
  
</head>
<body>
<h1>Hurra! I guess! Your number is {guess} in {counter} turns!</h1>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])

def index():
    if request.method == "GET":
        return html_start.format(0, 1000)  # DLACZEGO?????????

    if request.method == "POST":

        mini = int(request.form.get("min"))
        maxi = int(request.form.get("max"))
        guess = int(request.form.get("guess", 500))

        counter = int(request.form.get("counter", 1))
        answer = request.form.get("answer")



        if answer == "Too Big":
            maxi = guess
            counter += 1

        elif answer == "Too Small":
            mini = guess
            counter += 1
        elif answer == "Correct":
            return html_win.format(guess=guess, counter=counter)
 

        guess = (maxi - mini) // 2 + mini
        return HTML_GAME.format(guess=guess, min=mini, max=maxi, counter=counter)


if __name__ == '__main__':
    app.run()
