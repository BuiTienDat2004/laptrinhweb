from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/convert', methods=['GET', 'POST'])
def convert_temperature():
    result = None
    if request.method == 'POST':
        temp = float(request.form['temperature'])
        conversion_type = request.form['conversion']
        if conversion_type == 'CtoF':
            result = f"{temp}°C = {round(temp * 9 / 5 + 32, 2)}°F"
        elif conversion_type == 'FtoC':
            result = f"{temp}°F = {round((temp - 32) * 5 / 9, 2)}°C"
    return render_template('temperature.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
