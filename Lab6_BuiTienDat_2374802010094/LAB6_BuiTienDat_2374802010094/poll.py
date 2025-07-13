from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Store votes in a dictionary
votes = {
    "Cats": 0,
    "Dogs": 0
}

@app.route('/poll', methods=['GET', 'POST'])
def poll():
    if request.method == 'POST':
        choice = request.form['option']
        if choice in votes:
            votes[choice] += 1
        return redirect('/poll')

    total_votes = sum(votes.values())
    percentages = {}
    for option, count in votes.items():
        if total_votes > 0:
            percentages[option] = round((count / total_votes) * 100, 1)
        else:
            percentages[option] = 0
    return render_template('poll.html', votes=votes, percentages=percentages)

if __name__ == '__main__':
    app.run(debug=True)
