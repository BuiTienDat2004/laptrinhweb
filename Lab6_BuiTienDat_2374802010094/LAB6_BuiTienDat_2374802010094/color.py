from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/color', methods=['GET', 'POST'])
def change_color():
    color = 'white'  # Default background
    if request.method == 'POST':
        color = request.form.get('color') or 'white'
    return render_template('color.html', color=color)

if __name__ == '__main__':
    app.run(debug=True)
