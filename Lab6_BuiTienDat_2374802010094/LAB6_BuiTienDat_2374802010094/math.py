from flask import Flask, render_template

app = Flask(__name__)

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    result = num1 + num2
    return render_template('math.html', num1=num1, num2=num2, result=result)

if __name__ == '__main__':
    app.run(debug=True)
