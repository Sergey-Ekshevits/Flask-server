from flask_wtf import FlaskForm
from wtforms import StringField, SearchField, SubmitField, BooleanField,PasswordField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    email=StringField("E-mail", validators=[Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=4,max=99)])
    rememberme = BooleanField("Запомнить меня", default=False)
    submit = SubmitField("Войти")