from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '6CcDPvaf5JlVv1xsCyAE6FSDWGXXG8kLt3PmcBM1v0FrOYcmlw'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost/registro_alunos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)




