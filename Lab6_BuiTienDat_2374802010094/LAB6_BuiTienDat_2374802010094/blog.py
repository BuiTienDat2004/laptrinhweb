from flask import Flask, render_template, abort

app = Flask(__name__)

# Sample blog posts dictionary
posts = {
    1: {"title": "First Post", "content": "Hello, world!"},
    2: {"title": "Second Post", "content": "This is another blog entry."},
    3: {"title": "Third Post", "content": "Flask is fun!"}
}

@app.route('/post/<int:post_id>')
def show_post(post_id):
    post = posts.get(post_id)
    if post:
        return render_template('blog.html', post=post)
    else:
        abort(404, description="Post not found")

if __name__ == '__main__':
    app.run(debug=True)
