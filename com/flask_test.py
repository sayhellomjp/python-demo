from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_view():
    return '''<form action='/signin' method='post'>
    <p><input type='text' name='username'/></p>
    <p><input type='password' name='password'/></p>
    <p><button type='submit'>submit</button></p>
    </form>'''

@app.route('/signin', methods=['POST'])
def signin_form():
    if request.form['username'] == 'admin' and request.form['password'] == '123':
        return '<h1>Hello admin</h1>'
    return '<h1>wrong pwd</h1>'

if __name__ == '__main__':
    app.run()
