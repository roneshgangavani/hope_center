from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired


class RegisterForm(FlaskForm):
    name = StringField("Name",
                       validators=[DataRequired(message="Please enter name")])
    email = StringField("Email",
                        validators=[
                            DataRequired(message="Please enter email"),
                            Email(message="Please enter valid email id")
                        ])
    password = PasswordField(
        "Password", validators=[DataRequired(message="Please enter password")])

    submit = SubmitField("Sign up")
