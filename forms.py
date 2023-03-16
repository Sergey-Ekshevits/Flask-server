from flask_wtf import FlaskForm
from wtforms import StringField, SearchField, SubmitField, BooleanField,PasswordField, SelectField, EmailField, SelectMultipleField, widgets
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired, Email, Length
from flask_ckeditor import CKEditorField
# import email_validator
# from wtforms.fields.html5 import EmailField
# from flask_uploads import UploadSet, IMAGES
# images = UploadSet('images', IMAGES)
class SelectFieldMultiCheckbox(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()
class LoginForm(FlaskForm):
    email=EmailField("E-mail", validators=[DataRequired(), Email(message='Only e-mail is allowed, e.g test@test.py')])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=4,max=99)])
    rememberme = BooleanField("Запомнить меня", default=False)
    submit = SubmitField("Войти")

class RegisterForm(FlaskForm):
    email=EmailField("E-mail", validators=[DataRequired(), Email(message='Only e-mail is allowed, e.g test@test.py')])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=4,max=99)])
    passwordrpt = PasswordField("Repeat password", validators=[DataRequired(), Length(min=4,max=99)])
    name = StringField("Имя", validators=[DataRequired(), Length(min=3,max=99)])
    submit = SubmitField("Регистрация")
class SearchForm(FlaskForm):
    search_field=SearchField("Поиск", validators=[DataRequired()])
    submit = SubmitField("Search")
class ChangeProfileForm(RegisterForm):
    submit = SubmitField("Внедрить изменения")
# , validators=[FileAllowed(['jpg','jpeg','png'])
class PostField(FlaskForm):
    title = StringField("Post title", validators=[DataRequired(),Length(min=4,max=99)])
    body = CKEditorField("Body", validators=[DataRequired(), Length(min=20,max=1199)])
    post_pic = FileField('Post picture', default=None, validators=[FileAllowed(['jpg','jpeg','png'],"Only images!")])
    category = SelectFieldMultiCheckbox ('Категории', default=None, coerce=int)
    submit = SubmitField("Отправить")

class CommentField(FlaskForm):
    content = StringField("Comment", validators=[DataRequired(), Length(min=4,max=400)])
    submit = SubmitField("Комментировать")
class SelectPostsFilter(FlaskForm):
    my_post = BooleanField('My Posts', default="checked")
    selection = SelectField('Select posts', choices=[('all','All posts'),('last_day', 'Last day'),('last_week','Last week'),('last_month', 'Last month')])
    submit = SubmitField("Искать")

class CategoryFilter(FlaskForm):
    category = BooleanField('Categories', default="checked")