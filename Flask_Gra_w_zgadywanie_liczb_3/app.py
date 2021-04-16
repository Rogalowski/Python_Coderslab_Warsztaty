from flask import Flask, request
import random

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def zgadywanka():
    if request.method == 'GET':
        return ''' 
    <html> 
        <body>
            <form method = "POST">
            <input type="maxi"  name = "maxi" >
            <input type="mini"  name = "mini" >
            <input type="guess"  name = "guess" >
            
            <input type = "submit">
            </form >
        </body>
    </html>
    '''


    #if request.method == 'POST':
    else:
        liczba_wprowadzona = int(request.form["liczba_wprowadzona"])
        if liczba_wprowadzona == liczba_losowa:
            return f"TRAFILES Wylosowana liczba: {liczba_losowa} Wprowadzona: {liczba_wprowadzona}"
        elif liczba_wprowadzona < liczba_losowa:
            return f"NIETRAFILES ZA MALO, Wylosowana liczba: {liczba_losowa} Wprowadzona: {liczba_wprowadzona}"
        elif liczba_wprowadzona > liczba_losowa:
            return f"NIETRAFILES ZA DUZO, Wylosowana liczba: {liczba_losowa} Wprowadzona: {liczba_wprowadzona}"
        #liczba1 = int(liczba1)


    # else:
    #     return f"To nie ta liczba {liczba_wprowadzona}"





if __name__ == '__main__':
    app.run(debug=True, port=5002)