from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__, static_folder="static")

@app.route("/")
def main_page():
    return render_template("main.html")

if __name__ == '__main__':
    app.run(debug=True)