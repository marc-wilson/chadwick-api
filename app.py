from flask import Flask
from models import db, People

app = Flask(__name__)

#db.init_app(app)

@app.route('/')
def hello_world():
    #people = People.query.filter_by(birthYear=1986).all()
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
