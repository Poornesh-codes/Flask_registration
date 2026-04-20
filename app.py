#importing files(db.py and forms.py) and modules 
import os
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, flash
from forms import RegisterForm
from models import db, User
from datetime import datetime
#creating app (flask object)
app = Flask(__name__)
#secret key is used for session and security
load_dotenv() # to load environment variables from .env file

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
# connecting to database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
#initialize db wit app
db.init_app(app)
#db.create_all() # to create the database and tables it ignores if database already exists
with app.app_context():
    db.create_all()

#creating routes and views (home,about and register)

#home route used datetime module to show current date and time something like 2026 03 16 14:30:46 on '\' or home page
# @app.route tells Flask which url should start the function
@app.route("/")
def home():
    now = datetime.now()
    format_date = now.strftime("%Y:%m:%d %H:%M:%S")
    return render_template("home.html", current_time=format_date)
#about route

@app.route("/about")
#connecting about route to about.html
def about():
    return render_template("about.html")

#registr route
@app.route("/register", methods=["GET","POST"])
def register():
    #creating form
    form = RegisterForm()
    #checks if form s valid and submitted And all validators are passed
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        #adding user to database 
        db.session.add(user)

        #after adding user to db ,commit changs to save it in db
        db.session.commit()

        #using flash to show message it is just like return "message" but it can be used to show msg on next page after submitting form
        flash("Registration successful!", "success")
        
        #redirts to success page(that is confirm.html)
        return redirect(url_for("registration_success", username=form.username.data))
    #if form not valid it will render back register page
    return render_template("register.html", form=form)

#success route
#using dynamic route <username> ,it will show 127...5000/success/nouseai (if username is nouseai) in the address bar

@app.route("/success/<username>")
def registration_success(username):
    return render_template("confirm.html", username=username)


if __name__ == "__main__":
    app.run(debug=True)