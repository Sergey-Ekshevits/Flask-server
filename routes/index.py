import calendar
import time
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from flask import Blueprint, render_template, request
from flask_login import current_user
from flask_paginate import Pagination
from sqlalchemy import desc

from settings import POSTS_PER_PAGE, LIMIT_CATEGORIES
from db.db import db
from db.models import Post, Category, ass_post_category
from forms import SelectPostsFilter

index = Blueprint(
    'index',
    __name__,
    template_folder='templates'
)

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


@index.route('/', methods=['GET'])
# @app.route('/<int:page>', methods = ['GET', 'POST'])
# @login_required
def index_page():
    page = request.args.get('page', 1, type=int)
    my_post = request.args.get('my_post', False, type=bool)
    selection = request.args.get("selection", "all", type=str)
    form = SelectPostsFilter(my_post=my_post, selection=selection)
    current_GMT = time.gmtime()
    time_stamp = calendar.timegm(current_GMT)
    time_to_check = datetime.fromtimestamp(time_stamp)
    query = Post.query
    cats = db.session.query(
        Category, db.func.count(ass_post_category.c.post_id).label('total')) \
        .join(ass_post_category) \
        .group_by(Category) \
        .order_by(desc('total')) \
        .limit(LIMIT_CATEGORIES).all()

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
                            per_page=POSTS_PER_PAGE,
                            css_framework="bootstrap5",
                            display_msg="посты <b>{start} - {end}</b> из \
<b>{total}</b>")
    return render_template(
        'index.html',
        current_user=current_user,
        title="Блог",
        menu=menu,
        total=total,
        pagination=pagination,
        paginated=paginated,
        form=form,
        cats=cats
    )


@index.route('/search', methods=['GET'])
def search():
    searched = request.args.get('search_field')
    posts = []
    if searched:
        posts = Post.query.filter(
            Post.body.contains(searched)
            | Post.title.contains(searched)).order_by(Post.title).all()
    return render_template(
        "search_result.html",
        searched=searched,
        posts=posts)
