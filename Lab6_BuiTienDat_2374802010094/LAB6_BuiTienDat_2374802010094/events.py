from flask import Flask, render_template, request, redirect

app = Flask(__name__)

events = []  # List of event dictionaries: {name, date}

@app.route('/events', methods=['GET', 'POST'])
def event_list():
    if request.method == 'POST':
        name = request.form['name']
        date = request.form['date']
        if name and date:
            events.append({'name': name, 'date': date})
        return redirect('/events')
    return render_template('events.html', events=events)

if __name__ == '__main__':
    app.run(debug=True)
