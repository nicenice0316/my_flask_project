from flask import Flask, render_template, redirect, url_for
import config

app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def hello_world():
    # return 'Hello World!'
    # return {'user': '好的6678'}
    return redirect(url_for('about'))


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
