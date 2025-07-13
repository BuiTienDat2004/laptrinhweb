from flask import Flask, render_template, request, redirect

app = Flask(__name__)

entries = []  # Stores guestbook entries as list of dictionaries

@app.route('/guestbook', methods=['GET', 'POST'])
def guestbook():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        if name and message:
            entries.append({'name': name, 'message': message})
        return redirect('/guestbook')
    return render_template('guestbook.html', entries=entries)

if __name__ == '__main__':
    app.run(debug=True)
