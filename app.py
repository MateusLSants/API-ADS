from flask import Flask

app = Flask(__name__)
app.config['DEBUG']=True

@app.route('/', methods=['GET'])
def index():
    return '<h1>index<h1/>'

app.run()