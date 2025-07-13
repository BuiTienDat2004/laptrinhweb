from flask import Flask, render_template, request, redirect

app = Flask(__name__)

books = []  # List of dictionaries with title and author

@app.route('/books', methods=['GET', 'POST'])
def book_list():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        if title and author:
            books.append({'title': title, 'author': author})
        return redirect('/books')
    return render_template('books.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
