from flask import Flask, redirect, url_for, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = '185.95.31.122'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = ''

mySql = MySQL(app)


class Pauze:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end


def getPauzes():
    cursor = mySql.connection.cursor()
    cursor.execute("SELECT BeginPauze, eindePauze FROM Pauze;")
    pauses = []
    for (BeginPauze, eindePauze) in cursor:
        pauze = Pauze(BeginPauze, eindePauze)
        pauses.append(pauze)
        print(pauze.begin)
        print(pauze.end)
    cursor.close()
    return pauses


# @app.route("/home", methods=["POST", "GET"])
# def home():
#     if request.method == "POST":
#         begins = request.form["begin"]
#         end = request.form["end"]
#         time = request.form["time"]
#         cursor = mySql.connection.cursor()
#         # cursor.execute("INSERT INTO pauze (begin, einde, speling) VALUES (%s, %s, %s);", (begins, end, time))
#         mySql.connection.commit()
#         cursor.close()
#         return redirect(url_for("stoplicht"))
#     else:
#         pauses = getPauzes()
#         return render_template("index.html", pauses=pauses)


@app.route("/stoplicht")
def stoplicht():
    pauses = getPauzes()
    return render_template("stoplicht.html", pauses=pauses)


if __name__ == "__main__":
    app.run(debug=True)
