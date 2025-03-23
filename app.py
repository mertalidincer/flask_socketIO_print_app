import os
from flask import Flask, render_template
from flask_socketio import SocketIO
import db
import auth




app = Flask(__name__)
socketio = SocketIO(app)

app.config.from_mapping(
    SECRET_KEY=os.urandom(24),
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
)

db.init_app(app)
app.register_blueprint(auth.bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app, debug=True)