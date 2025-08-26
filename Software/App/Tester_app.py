# Bachelor Thesis - Web Application for Universal_Tester Board
# Institution: University of Pardubice
# Faculty: Faculty of Electrical Engineering and Informatics
# Department: Department of Electronics and Radio Systems
# Study Program: Applied Electrical Engineering
#
# Author: Daniel Brandejs
# GitHub: https://github.com/DanB254
# Date of Creation: 26.8.2025
# Project Partner: HARDWARIO A.S - https://www.hardwario.com/
#
# Repository: https://github.com/DanB254/BachelorThesis
# Version: 1.0
#
# Requirements:
#   - Python 3.x
#   - Flask
#   - pySerial
#   - UniTest Board - https://github.com/DanB254/BachelorThesis/tree/main/Hardware/Universal_Tester
#   - Linux OS (for /dev/ttyUSB0 port)

from flask import Flask, render_template, request
import serial

Board = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)

Tester_app = Flask(__name__)


@Tester_app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    if request.method == "POST":
        cmd = request.form["command"]
        # send the command to the board
        Board.write((cmd + "\n").encode())

        # try to read the response from the board
        if Board.in_waiting > 0:
            output = Board.readline().decode(errors="ignore").strip()

    return render_template("index.html", output=output)

if __name__ == "__main__":
    Tester_app.run(debug=True)