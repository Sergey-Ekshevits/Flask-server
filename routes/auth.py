from flask import Blueprint, render_template, abort

auth = Blueprint('auth', __name__,
                 template_folder='templates')


@auth.route('/authorization', methods=['GET', 'POST'])
def authorization():
    return render_template('authorization.html')
