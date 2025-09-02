from flask import Flask, jsonify
from src.routes.api import process_api


app = Flask(__name__)


app.register_blueprint(process_api,url_prefix='/api')

@app.route("/")
def test():
    return "<i>Hello test!</i>"




@app.errorhandler(404)
def not_found(e):
    return jsonify({
        "error": "Not Found",
        "message": "This route probably does not exist."
    }), 404


if __name__ == "__main__":
    app.run(debug=True)