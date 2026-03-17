# importing the file 

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
#importing EqualTo
from wtforms.validators import EqualTo
#creating registration form using FlaskForm and class RegisterForm inherits from FlaskForm it has objects username,email,password,confirm_password and submit
class RegisterForm(FlaskForm):

    username = StringField("Username",validators=[DataRequired(),Length(min=3, max=20)])
    """
    added data requred to make sure the field is not empty and len to make username (3-20)
    stringField is used to get string input from user
    """

    email = StringField(
        "Email",
        validators=[DataRequired(), Email()#checks if email valid (@,ending with .com)
                    ]

    )
    """
    added Email() to check if eemail is vaild ( it checks for @ and .com)
    """
    password = PasswordField(
        "Password",
        validators=[DataRequired(), 
                    Length(min=6)# min password length set to 6 char
                    ]
    )
    """
    added Length() to set minimum password length to 6 chars
    data required to make sure the password is not empty
    passwordField is used so that input is hidden like this (****) when typing actual password
    """
    #to comfirm the password
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[DataRequired(), 
                    EqualTo("password")#checks if password matches (str compare with password and confirm_password) 
                    ]
    )
    #submit button 
    submit = SubmitField("Register")
    