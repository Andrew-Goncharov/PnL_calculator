from flask import Flask
from flask import render_template

app = Flask(__name__,
            static_folder="../web/static",
            template_folder="../web/templates")


@app.route("/")
def main():
    return render_template("index.html")
