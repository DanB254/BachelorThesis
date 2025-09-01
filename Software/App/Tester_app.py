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

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# počáteční stav slideru
slider_state = "Test/Debug"

@app.route("/")
def index():
    return render_template("index.html", state=slider_state)

@app.route("/slider_state", methods=["POST"])
def slider_state_update():
    global slider_state
    data = request.get_json()
    slider_state = data.get("state", "Test/Debug")
    print("Slider state:", slider_state)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
