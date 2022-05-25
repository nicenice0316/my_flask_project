from flask import Blueprint, render_template, request
from exts import mail
from flask_mail import Message

import string
import random


bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/login')
def login():
    return render_template('login.html')


@bp.route('/register')
def register():
    return render_template('register.html')


@bp.route('/get_captcha')
def get_captcha():
    email = request.args.get('email')
    letters = string.ascii_letters + string.digits
    captcha = ''.join(random.sample(letters, 4))
    message = Message(subject='flask 邮箱测试',
                      recipients=[email],
                      body=f'验证码是{captcha}，5分钟内有效')
    mail.send(message)

    return 'success'
