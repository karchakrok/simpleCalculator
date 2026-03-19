from flask import *

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def login1():
    return render_template('login.html')

@app.route('/', methods=['POST'])
def login2():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login1'))
        
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/calc', methods=['GET'])
def calc():
    return render_template('calc.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')