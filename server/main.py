from flask import *
import sqlite3
from datetime import datetime

app = Flask(__name__)


@app.route('/add/stream', methods=["GET", "POST"])
def addStream():
    if request.method == 'POST':
        streamValue = request.form['streamValue']
        with sqlite3.connect('database.db') as conn:
            try:
                cur = conn.cursor()
                cur.execute('''INSERT INTO stream (streamValue,eventTime) VALUES (?, ?)''',
                            (streamValue, datetime.now()))
                conn.commit()
                msg = "added successfully"
            except:
                msg = "error occured"
                conn.rollback()
        conn.close()
    return msg


@app.route('/add/voltage', methods=["GET", "POST"])
def addVoltage():
    if request.method == 'POST':
        voltageValue = request.form['voltageValue']
        with sqlite3.connect('database.db') as conn:
            try:
                cur = conn.cursor()
                cur.execute('''INSERT INTO voltage (voltageValue,eventTime) VALUES (?, ?)''',
                            (voltageValue, datetime.now()))
                conn.commit()
                msg = "added successfully"
            except:
                msg = "error occured"
                conn.rollback()
        conn.close()
    return msg


@app.route('/add/humidity', methods=["GET", "POST"])
def addHumidity():
    if request.method == 'POST':
        humidityValue = request.form['humidityValue']
        with sqlite3.connect('database.db') as conn:
            try:
                cur = conn.cursor()
                cur.execute('''INSERT INTO humidity (humidityValue,eventTime) VALUES (?, ?)''',
                            (humidityValue, datetime.now()))
                conn.commit()
                msg = "added successfully"
            except:
                msg = "error occured"
                conn.rollback()
        conn.close()
    return msg


@app.route('/add/rain', methods=["GET", "POST"])
def addRain():
    if request.method == 'POST':
        rainValue = request.form['rainValue']
        with sqlite3.connect('database.db') as conn:
            try:
                cur = conn.cursor()
                cur.execute('''INSERT INTO rain (action,eventTime) VALUES (?, ?)''', (rainValue, datetime.now()))
                conn.commit()
                msg = "added successfully"
            except:
                msg = "error occured"
                conn.rollback()
        conn.close()
    return msg


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
    return msg


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
    return msg


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
    return msg


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
    return msg


@app.route("/check/<int:power>/<int:voltage>/<int:stream>")
def check(power, voltage, stream):
    power1 = voltage * stream

    if (power < power1):
        return "1"
    else:
        return "0"


@app.route("/std/angel_information")
def angel_information():
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT angelValue, eventTime FROM angel')
        Data = cur.fetchall()
    return jsonify(Data)


@app.route("/std/power_information")
def power_information():
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT powerValue, eventTime FROM power')
        Data = cur.fetchall()
    return jsonify(Data)


@app.route("/std/stream_information")
def stream_information():
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT streamValue, eventTime FROM stream')
        Data = cur.fetchall()
    return jsonify(Data)


@app.route("/std/voltage_information")
def voltage_information():
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT voltageValue, eventTime FROM voltage')
        Data = cur.fetchall()
    return jsonify(Data)


if __name__ == '__main__':
    app.run(debug=True)
