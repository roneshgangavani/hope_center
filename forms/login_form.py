from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    email = StringField("Email",
                        validators=[
                            DataRequired(message="Please enter email"),
                            Email(message="Please enter valid email")
                        ])
    password = PasswordField(
        "Password", validators=[DataRequired(message="Please enter password")])
    submit = SubmitField("Sign In")