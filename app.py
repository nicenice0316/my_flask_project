from flask import Flask
import config
from exts import db
from blueprints import user_bp
from blueprints import qa_bp

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

app.register_blueprint(user_bp)
app.register_blueprint(qa_bp)
# migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run()
