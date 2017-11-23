from flask import Flask,send_file
from flask import abort
from flask import redirect

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('templates/index.html')

@app.route('/user/<name>')
def sayHello(name):
    if name == 'baidu':
        return redirect('http://www.baidu.com')
    elif name == 'NO':
        return abort(404)
    return '<h1> hello,%s </h1>' % name

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8081,debug=True)
