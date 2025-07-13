from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []  # List of dictionaries, each with 'task' and 'completed' status

@app.route('/todo', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        if 'new_task' in request.form:
            task_name = request.form['new_task']
            if task_name:
                tasks.append({'task': task_name, 'completed': False})
        elif 'toggle' in request.form:
            index = int(request.form['toggle'])
            tasks[index]['completed'] = not tasks[index]['completed']
        return redirect('/todo')
    
    return render_template('todolist.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
