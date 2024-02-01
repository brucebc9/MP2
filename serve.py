from flask import Flask, redirect, url_for, request, render_template, jsonify, session
import sys
import subprocess
import socket

app = Flask(__name__)
app.secret_key = "secretkey"


@app.route("/", methods=['POST', 'GET'])
def home():
    hostName = socket.gethostname()
    ipaddr = socket.gethostbyname(hostName)

    if request.method == 'POST':
        subprocess.run(["./stress_cpu.py"], shell=True, capture_output=True, text=True)
        return redirect(url_for("home"))
    else:
        return ipaddr


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
