from flask import Flask, render_template

app = Flask(__name__)

@app.route('/name/<username>')
def show_name(username):
    return render_template('name.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
