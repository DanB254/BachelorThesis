# Bachelor Thesis - Web Application for UniTest Board
# Institution: University of Pardubice
# Faculty: Faculty of Electrical Engineering and Informatics
# Department: Department of Electronics and Radio Systems
# Study Program: Applied Electrical Engineering
#
# Author: Daniel Brandejs
# GitHub: https://github.com/DanB254
#
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

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
