from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def linear_equation():
    x = -2
    y = 5 * x + 7
    return render_template('equation.html', x=x, y=y)

@app.route('/student')
def student_info():
    student = {
        'name': 'Bùi Tiến Đạt',
        'id': '2374802010094',
        'year': '2021-2025',
        'major': 'Công nghệ thông tin',
        'hobbies': ['Chơi Game', 'Loli', 'Đớp']
    }
    return render_template('student.html', student=student)

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get("username")
        return f"<h1>Form submitted!</h1><p>Hello, {username}!</p>"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

