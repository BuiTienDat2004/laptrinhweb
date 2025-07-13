from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = ''
    if request.method == 'POST':
        username = request.form['username']
    return render_template('login.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
