from flask import Flask, redirect, url_for, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'stoplicht'

mySql = MySQL(app)


class Pauze:
    def __init__(self, begin, end, time):
        self.begin = begin
        self.end = end
        self.time = time


def getPauzes():
    cursor = mySql.connection.cursor()
    cursor.execute("SELECT begin, einde, speling FROM pauze;")
    pauses = []
    for (begin, einde, speling) in cursor:
        pauze = Pauze(begin, einde, speling)
        pauses.append(pauze)
        print(pauze.begin)
        print(pauze.end)
        print(pauze.time)
    cursor.close()
    return pauses


@app.route("/home", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        begins = request.form["begin"]
        end = request.form["end"]
        time = request.form["time"]
        cursor = mySql.connection.cursor()
        cursor.execute("INSERT INTO pauze (begin, einde, speling) VALUES (%s, %s, %s);", (begins, end, time))
        mySql.connection.commit()
        cursor.close()
        return redirect(url_for("stoplicht"))
    else:
        pauses = getPauzes()
        return render_template("index.html", pauses=pauses)


@app.route("/stoplicht")
def stoplicht():
    pauses = getPauzes()
    return render_template("stoplicht.html", pauses=pauses)


@app.route("/templates")
def templates():
    render_template("stoplicht.js")


if __name__ == "__main__":
    app.run(debug=True)
