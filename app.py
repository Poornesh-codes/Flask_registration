from flask import Flask, render_template, redirect, url_for, flash
from forms import RegisterForm
from models import db, User
from datetime import datetime

app = Flask(__name__)

app.config["SECRET_KEY"] = "secret123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    now = datetime.now()
    format_date = now.strftime("%Y:%m:%d %H:%M:%S")
    return render_template("home.html", current_time=format_date)



@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/register", methods=["GET","POST"])
def register():

    form = RegisterForm()

    if form.validate_on_submit():

        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )

        db.session.add(user)
        db.session.commit()

        flash("Registration successful!", "success")

        return redirect(url_for("registration_success", username=form.username.data))

    return render_template("register.html", form=form)


@app.route("/success/<username>")
def registration_success(username):
    return render_template("confirm.html", username=username)


if __name__ == "__main__":
    app.run(debug=True)