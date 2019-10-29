from flask import Flask, render_template, request
import datetime

app = Flask(__name__)


@app.route("/")
def index():
    welcometext = "Herzlich Willkommen!"
    currentyear = datetime.datetime.now().year
    vemap = ["Martin", "Felix", "Anna", "Markus", "Yevgen"]
    rich = True
    return render_template("index.html", welcometext=welcometext, currentyear=currentyear, vemap=vemap, rich=rich)


@app.route("/about-me", methods=["GET"])
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST"])
def contact():
    contact_name = request.form.get("contact-name")
    contact_email = request.form.get("contact-email")
    contact_message = request.form.get("contact-message")
    print(contact_name)
    print(contact_email)
    print(contact_message)
    return render_template("success.html")

@app.route("/kaboom")
def kaboom():
    return render_template("kaboom.html")


if __name__ == '__main__':
    app.run()
