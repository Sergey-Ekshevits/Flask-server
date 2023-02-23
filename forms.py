from flask_wtf import FlaskForm
from wtforms import StringField, SearchField, SubmitField, BooleanField,PasswordField
from wtforms.validators import DataRequired, Email, Length
from flask_ckeditor import CKEditorField

class LoginForm(FlaskForm):
    email=StringField("E-mail", validators=[Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=4,max=99)])
    rememberme = BooleanField("Запомнить меня", default=False)
    submit = SubmitField("Войти")

class RegisterForm(FlaskForm):
    email=StringField("E-mail", validators=[Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=4,max=99)])
    passwordrpt = PasswordField("Repeat password", validators=[DataRequired(), Length(min=4,max=99)])
    name = StringField("Имя", validators=[DataRequired(), Length(min=3,max=99)])
    submit = SubmitField("Регистрация")
class SearchForm(FlaskForm):
    search_field=SearchField("Поиск", validators=[DataRequired()])
    submit = SubmitField("Search")
class ChangeProfileForm(RegisterForm):
    submit = SubmitField("Внедрить изменения")

class PostField(FlaskForm):
    title = StringField("Post title", validators=[DataRequired(),Length(min=4,max=99)])
    body = CKEditorField("Body", validators=[DataRequired(), Length(min=20,max=1199)])
    submit = SubmitField("Отправить")
