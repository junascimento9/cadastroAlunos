from flask import Flask 

app = Flask(__name__) 
app.config['SECRET_KEY'] = '6CcDPvaf5JlVv1xsCyAE6FSDWGXXG8kLt3PmcBM1v0FrOYcmlw'

from app import routes