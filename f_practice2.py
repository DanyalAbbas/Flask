from flask import Flask, redirect, url_for, render_template


app = Flask(__name__)


@app.route("/<name>")
def home(name):
    return render_template("index.html", content=name, r=2, hell=["chigga", "Danyal", "Zainab"])

# @app.route("/admin")
# def admin():
#     return redirect(url_for("user", name="Admin!"))




if __name__ == "__main__":
    app.run()