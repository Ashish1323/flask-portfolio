from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)
print(__name__)


@app.route("/")
def home():
    return render_template("index.html")


# dynamic routes!
@app.route("/<name>")
def all(name):
    return render_template(name + ".html")


@app.route("/submit", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
        return redirect("./thanks")


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
