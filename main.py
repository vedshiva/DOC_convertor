from flask import Flask, render_template, request
from livereload import Server

app = Flask(__name__, template_folder='Template')

app.secret_key = "12121"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("navi.html")

@app.route("/contact")
def contact():
    return render_template("navi.html")

@app.route("/service")
def service():
    return render_template("navi.html")

if __name__ == "__main__":
    server = Server(app.wsgi_app)
    server.watch('Template/*')  # optional: watch templates for reload
    server.serve(port=5000, host='127.0.0.1', debug=True)