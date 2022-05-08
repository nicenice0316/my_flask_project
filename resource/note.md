# 模板笔记

## 一、基本使用
1. 模板文件，也就是html文件，需要放在template文件夹下，也可以`app = Flask(__name__, template_folder='')`
修改
2. 通过`render_template`来渲染模板
3. 变量传递到模板中`context = {'username': 'alex'} return render_template('about.html', **context)`

## 二、ORM
1.  模型创建完成之后，使用`db.create_all()`来生成数据库表

## 三、一些注意点
1.  静态资源必须放在static里面，图片，css等

## 四、migrate数据库迁移
0.  `db.drop_all() db.create_all()`没有使用migrate的时候，用这个来创建表
1.  pip 安装 flaks-migrate
2.  flask db init 初始化，只需要第一次做。后面只需要执行3,4即可
3.  flask db migrate -m "first commit" 生成执行表的py文件
4.  flask db upgrade 执行真正的数据库操作

## 五、session 和 cookie
1.  在flask中，session是先把数据加密，然后用session_id作为key，存放到cookie中