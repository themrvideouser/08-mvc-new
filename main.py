from flask import Flask, render_template, request, make_response
import datetime

app = Flask(__name__)


@app.route("/")
def index():
    welcometext = "Herzlich Willkommen!"
    currentyear = datetime.datetime.now().year
    vemap = ["Martin", "Felix", "Anna", "Markus", "Yevgen"]
    rich = True
    return render_template("index.html", welcometext=welcometext, currentyear=currentyear, vemap=vemap, rich=rich)


@app.route("/about-me", methods=["GET", "POST"])
def about():
    if request.method == "GET":
        user_name = request.cookies.get("user_name")
        return render_template("about.html", name=user_name)
    elif request.method == "POST":
        contact_name = request.form.get("contact-name")
        contact_email = request.form.get("contact-email")
        contact_message = request.form.get("contact-message")
        print(contact_name)
        print(contact_email)
        print(contact_message)
        response = make_response(render_template("success.html"))
        response.set_cookie("user_name", contact_name)
        return response

@app.route("/kaboom")
def kaboom():
    return render_template("kaboom.html")


if __name__ == '__main__':
    app.run()
