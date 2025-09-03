from flask import Flask, jsonify, render_template
from src.routes.api import process_api


app = Flask(__name__,template_folder="../templates")


app.register_blueprint(process_api,url_prefix='/api')

@app.route("/")
def test():
    return "<i>Hello test!</i>"




@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)