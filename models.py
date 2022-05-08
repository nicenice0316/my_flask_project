from exts import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    note = db.Column(db.String(200), nullable=False)


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
