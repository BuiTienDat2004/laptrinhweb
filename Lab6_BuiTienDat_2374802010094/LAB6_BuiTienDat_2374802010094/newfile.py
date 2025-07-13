from flask import Flask, render_template

app = Flask(__name__)

@app.route('/new')
def new_page():
    return render_template('newfile.html')

if __name__ == '__main__':
    app.run(debug=True)
