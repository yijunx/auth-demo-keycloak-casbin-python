from flask import Flask
from app.apis.oidc_api import bp as oidc_bp

app = Flask(__name__)


# well nihao is working
@app.route("/nihao")
def nihao():
    return "nihao"


app.register_blueprint(blueprint=oidc_bp)