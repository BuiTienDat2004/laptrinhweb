from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []

@app.route('/tasks', methods=['GET', 'POST'])
def task_list():
    if request.method == 'POST':
        task = request.form['task']
        if task:
            tasks.append(task)
        return redirect('/tasks')
    return render_template('tasklist.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
