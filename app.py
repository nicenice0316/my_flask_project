from flask import Flask, render_template, redirect, url_for
from flask_migrate import Migrate
from models import Article, User, UserExtension
import config
from apps.book import bp as book_bp
from apps.course import bp as course_bp
from apps.user import bp as user_bp
import datetime
from exts import db

app = Flask(__name__)
app.config.from_object(config)

app.register_blueprint(book_bp)
app.register_blueprint(course_bp)
app.register_blueprint(user_bp)

# 把app绑定到db上
db.init_app(app)
migrate = Migrate(app, db)





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
