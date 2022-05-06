from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config
from apps.book import bp as book_bp
from apps.course import bp as course_bp
from apps.user import bp as user_bp
import datetime

app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(book_bp)
app.register_blueprint(course_bp)
app.register_blueprint(user_bp)

db = SQLAlchemy(app)

migrate = Migrate(app, db)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)


class UserExtension(db.Model):
    __tablename__ = 'user_extension'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    school = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # userlist=False，代表反向引用的时候，不是一个礼拜，而是一个对象
    user = db.relationship('User', backref=db.backref('extension', uselist=False))


# 定义ORM模型
class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # 1、 第一个参数是模型名字，必须要和模型的名字保持一致
    # 2、 backref，代表反向引用，代表对方访问我的时候的名字
    author = db.relationship('User', backref='articles')


# db.drop_all()
# db.create_all()


@app.route('/otm')
def one_to_many():
    now = datetime.datetime.now().strftime('%Y:%m:%d_%H:%M:%S')
    article = Article(title='这是第一个文章', content='打印一下时间吧 ' + now)
    user = User(username='Jack')
    article.author = user
    # user数据会自动添加
    db.session.add(article)
    db.session.commit()
    print(user.articles)
    return 'one to many 数据操作成功'


@app.route('/oto')
def one_to_one():
    # user = User.query.filter_by(id=1).first
    user = User(username='Jack')
    extension = UserExtension(school='清华大学')
    user.extension = extension
    db.session.add(user)
    db.session.commit()
    return 'one to one 数据操作成功'


@app.route('/article')
def article_view():
    # 1、添加数据
    # now = datetime.datetime.now().strftime('%Y:%m:%d_%H:%M:%S')
    # article = Article(title='这是第一个文章', content='打印一下时间吧 ' + now)
    # db.session.add(article)
    # db.session.commit()

    # 2、查询
    # filter_by返回一个列表对象
    # article = Article.query.filter_by(id=1)[0]
    # print(article.title)
    # print(article.content)

    # 3、修改
    # article = Article.query.filter_by(id=1)[0]
    # print('修改前_', article.content)
    # article.content = '随便修改一下吧'
    # db.session.commit()

    # 4、删除
    # Article.query.filter_by(id=1).delete()
    # db.session.commit()

    return '数据操作成功'


@app.route('/helloworld')
def hello_world():
    now = datetime.datetime.now().strftime('%Y:%m:%d_%H:%M:%S')
    print(now)
    # return 'Hello World!'
    # return {'user': '好的6678'}
    return redirect(url_for('about'))


@app.route('/')
def index():
    # 测试数据库连接
    # engine = db.get_engine()
    # conn = engine.connect()
    # conn.close()
    # with engine.connect() as conn:
    #     result = conn.execute('select 1')
    #     print(result.fetchone())
    # return render_template('index.html')
    return render_template('login.html')


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
