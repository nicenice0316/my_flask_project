from flask import Blueprint, render_template

bp = Blueprint('book', __name__, url_prefix='/book')


@bp.route('/list')
def book_list():
    return render_template('book_list.html')

