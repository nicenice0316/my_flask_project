# 模板笔记

## 一、基本使用
1. 模板文件，也就是html文件，需要放在template文件夹下，也可以`app = Flask(__name__, template_folder='')`
修改
2. 通过`render_template`来渲染模板
3. 变量传递到模板中`context = {'username': 'alex'} return render_template('about.html', **context)`