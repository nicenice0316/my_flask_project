from flask import Blueprint

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/login')
def user_list():
    return '登录'
