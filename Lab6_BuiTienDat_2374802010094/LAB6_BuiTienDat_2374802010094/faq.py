from flask import Flask, render_template, abort

app = Flask(__name__)

# Example FAQ dictionary
faqs = {
    1: {"question": "What is Flask?", "answer": "A lightweight web framework for Python."},
    2: {"question": "How do I install Flask?", "answer": "Run 'pip install flask' in your terminal."},
    3: {"question": "Is Flask good for beginners?", "answer": "Yes, it's simple and powerful!"}
}

@app.route('/faq/<int:question_id>')
def faq(question_id):
    entry = faqs.get(question_id)
    if entry:
        return render_template('faq.html', faq=entry)
    else:
        abort(404, description="FAQ not found")

if __name__ == '__main__':
    app.run(debug=True)
