from flask import Flask, render_template, url_for, redirect, request
import csv

app = Flask(__name__)
print(__name__)


@app.route("/")
def home():
    return render_template("index.html")


# dynamic routes!
@app.route("/<name>")
def all(name):
    return render_template(name + ".html")


def write_data(data):
    with open("database.txt", mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n {email},{subject},{message}")


@app.route("/submit", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        data = request.form.to_dict()
        write_data(data)
        return redirect("./thanks")


def write_to_csv(data):
    with open("database.csv", newline="", mode="a") as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(
            csv,
            delimiter=",",
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL,
            newline="",
        )
        csv_writer.writeheader()
        csv_writer.writerow([email, subject, message])


# @app.route("/works")
# def works():
#     return render_template("works.html")


# @app.route("/work")
# def work():
#     return render_template("work.html")


# @app.route("/about")
# def about():
#     return render_template("about.html")


# @app.route("/contact")
# def contact():
#     return render_template("contact.html")


# @app.route("/components")
# def components():
#     return render_template("components.html")
