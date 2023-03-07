import calendar
import time
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta
from flask import Flask
from flask import render_template, request
from flask_login import LoginManager, current_user, login_required
# from flask_marshmallow import Marshmallow
from forms import SearchForm
from flask_migrate import Migrate
from flask_ckeditor import CKEditor
from flask_paginate import Pagination
from forms import SelectPostsFilter
from flask_jwt_extended import JWTManager
# import all models for migrate TODO need to fix
from db.Category import Category
from db.Post import Post
from db.User import User
from db.db import ma
from db.db import db
from routes.api import api
from routes.auth import auth
from routes.posts import post
import bot
import threading
import os
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()
DATABASE = 'blogdb2.db'
DEBUG = False
SECRET_KEY = os.getenv('SECRET_KEY')

app = Flask(__name__)
app.register_blueprint(auth)
app.register_blueprint(post)
app.register_blueprint(api)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(app.root_path, DATABASE)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app_ctx = app.app_context()
app_ctx.push()
db.init_app(app)
app.secret_key = SECRET_KEY

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Авторизуйтесь для доступа к странице'
login_manager.login_message_category = 'success'
migrate = Migrate(app, db)
ckeditor = CKEditor(app)
POSTS_PER_PAGE = 4

CORS(app)
jwt = JWTManager(app)
app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET_KEY')  # Change this!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
ma(app)
class TelegramThread(threading.Thread):
    def run(self) -> None:
        bot.run_bot(app_ctx)

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', menu=menu, title='Страница не найдена')


@app.errorhandler(500)
def page_not_found2(error):
    return render_template('404.html', menu=menu, title='Страница не найдена')


menu = [
    {
        "name": "Главная",
        "link": "/"
    },
    {
        "name": "О нас",
        "link": "/"
    },
    {
        "name": "Авторизация",
        "link": "/authorization"
    }
]


@app.context_processor
def base():
    search_form = SearchForm()
    return dict(search_form=search_form)


@app.route('/', methods=['GET'])
# @app.route('/<int:page>', methods = ['GET', 'POST'])
# @login_required
def index():
    page = request.args.get('page', 1, type=int)
    my_post = request.args.get('my_post', False, type=bool)
    selection = request.args.get("selection", "all", type=str)
    form = SelectPostsFilter(my_post=my_post, selection=selection)
    current_GMT = time.gmtime()
    time_stamp = calendar.timegm(current_GMT)
    time_to_check = datetime.fromtimestamp(time_stamp)
    query = Post.query
    if request.method == "GET":
        if selection == 'last_month':
            ts = str(datetime.timestamp(time_to_check + relativedelta(months=-1)))
            query = query.filter(Post.date_created >= ts)
        if selection == 'last_week':
            ts = str(datetime.timestamp(time_to_check + relativedelta(weeks=-1)))
            query = query.filter(Post.date_created >= ts)
        if selection == 'last_day':
            ts = str(datetime.timestamp(time_to_check + relativedelta(days=-1)))
            query = query.filter(Post.date_created >= ts)
    if my_post and current_user:
        query = query.filter(Post.owner == current_user.id)
    query = query.order_by(Post.date_created.desc())
    total = query.count()
    paginated = query.paginate(page=page, per_page=POSTS_PER_PAGE)
    pagination = Pagination(page=page, total=total,
                            per_page=POSTS_PER_PAGE, css_framework="bootstrap5", display_msg="посты <b>{start} - {end}</b> из \
<b>{total}</b>")
    return render_template(
        'index.html',
        current_user=current_user,
        title="Блог",
        menu=menu,
        total=total,
        pagination=pagination,
        paginated=paginated,
        form=form
    )


@app.route('/search', methods=['GET'])
def search():
    searched = request.args.get('search_field')
    posts = []
    if searched:
        posts = Post.query.filter(Post.body.contains(searched) | Post.title.contains(searched)).order_by(
            Post.title).all()
    return render_template("search_result.html", searched=searched, posts=posts)



@app.template_filter('formatdatetime')
def format_datetime(value, format="%d %b %Y %I:%M %p"):
    """Format a date time to (Default): d Mon YYYY HH:MM P"""
    if value is None:
        return ""
    return datetime.fromtimestamp(int(value)).strftime(format)


@app.template_filter('timedif')
def time_difference(value, format="%d %b %Y %I:%M %p"):
    now = datetime.now()
    # timedif=now-datetime.fromtimestamp(int(value))
    # timedif_hours = timedif.hours()
    delta = now - datetime.fromtimestamp(int(value))
    if delta.total_seconds() / 1800 < 1:
        return "less than 30 min ago"
    else:
        return datetime.fromtimestamp(int(value)).strftime(format)


@app.template_filter('deletescript')
def deletescript(value):
    if value is None:
        return ""
    return value.replace("script", "p")


if __name__ == '__main__':
    bot_run = TelegramThread(daemon=True)
    # bot_run.start()
    app.run(host="0.0.0.0", debug=True)
