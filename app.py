from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import config
from apps.book import bp as book_bp
from apps.course import bp as course_bp
from apps.user import bp as user_bp

app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(book_bp)
app.register_blueprint(course_bp)
app.register_blueprint(user_bp)

db = SQLAlchemy(app)

@app.route('/helloworld')
def hello_world():
    # return 'Hello World!'
    # return {'user': '好的6678'}
    return redirect(url_for('about'))


@app.route('/')
def index():
    # 测试数据库连接
    engine = db.get_engine()
    # conn = engine.connect()
    # conn.close()
    with engine.connect() as conn:
        result = conn.execute('select 1')
        print(result.fetchone())
    return render_template('index.html')


@app.route('/about')
def about():
    # 模板必须放在templates文件夹下。也可以设置
    # app = Flask(__name__, template_folder='')
    # 上下文context
    context = {'username': 'alex'}
    return render_template('about.html', **context)


@app.route('/control')
def control():
    context = {'age': 16,
               'books': ['红楼梦', '西游记', '水浒传', '三国演义'],
               'person': {'name': 'jack', 'age': 18}}
    return render_template('control.html', **context)


if __name__ == '__main__':
    app.run()
