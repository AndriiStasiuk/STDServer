from flask import *
import sqlite3, hashlib, os
from datetime import datetime
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/add/power', methods=["GET", "POST"])
def addPower():
    if request.method == 'POST':
        powerValue = request.form['powerValue']
        with sqlite3.connect('database.db') as conn:
            try:
                cur = conn.cursor()
                cur.execute('''INSERT INTO power (powerValue,eventTime) VALUES (?, ?)''', (powerValue, datetime.now()))
                conn.commit()
                msg = "added successfully"
            except:
                msg = "error occured"
                conn.rollback()
        conn.close()
    return "Success"


@app.route('/add/angel', methods=["GET", "POST"])
def addAngel():
    if request.method == 'POST':
        angelValue = request.form['angelValue']
        with sqlite3.connect('database.db') as conn:
            try:
                cur = conn.cursor()
                cur.execute('''INSERT INTO angel (angelValue,eventTime) VALUES (?, ?)''', (angelValue, datetime.now()))
                conn.commit()
                msg = "added successfully"
            except:
                msg = "error occured"
                conn.rollback()
        conn.close()
    return "Success"


@app.route("/deletePower/<id>")
def removeInformationPower(id):
    with sqlite3.connect('database.db') as conn:
        try:
            cur = conn.cursor()
            cur.execute('DELETE FROM power WHERE id = ' + id)
            conn.commit()
            msg = "Deleted successsfully"
        except:
            conn.rollback()
            msg = "Error occured"
    conn.close()
    print(msg)
    return "Deleted successsfully"


@app.route("/deleteAngel/<id>")
def removeInformationAngel(id):
    with sqlite3.connect('database.db') as conn:
        try:
            cur = conn.cursor()
            cur.execute('DELETE FROM angel WHERE id = ' + id)
            conn.commit()
            msg = "Deleted successsfully"
        except:
            conn.rollback()
            msg = "Error occured"
    conn.close()
    print(msg)
    return "Deleted successsfully"


if __name__ == '__main__':
    app.run(debug=True)
