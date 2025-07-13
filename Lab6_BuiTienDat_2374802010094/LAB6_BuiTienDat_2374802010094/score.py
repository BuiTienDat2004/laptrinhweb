from flask import Flask, render_template

app = Flask(__name__)

@app.route('/score/<int:mark>')
def show_grade(mark):
    if mark >= 90:
        grade = 'A'
    elif mark >= 80:
        grade = 'B'
    elif mark >= 70:
        grade = 'C'
    elif mark >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return render_template('score.html', mark=mark, grade=grade)

if __name__ == '__main__':
    app.run(debug=True)
