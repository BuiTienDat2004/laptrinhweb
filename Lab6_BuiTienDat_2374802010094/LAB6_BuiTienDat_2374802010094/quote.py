from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

quotes = [
    "Believe you can and you're halfway there.",
    "The best way to get started is to quit talking and begin doing.",
    "Keep going. Everything you need will come to you.",
    "Your limitation—it's only your imagination.",
    "Push yourself, because no one else is going to do it for you."
]

@app.route('/quote', methods=['GET', 'POST'])
def quote():
    selected_quote = random.choice(quotes)
    if request.method == 'POST':
        return redirect(url_for('quote'))  # Redirect to trigger a new random quote
    return render_template('quote.html', quote=selected_quote)

if __name__ == '__main__':
    app.run(debug=True)
