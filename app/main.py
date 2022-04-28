from flask import Flask


app = Flask(__name__)


# well nihao is working
@app.route("/nihao")
def nihao():
    return "nihao"
