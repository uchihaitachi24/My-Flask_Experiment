from flask import Flask, render_template


app = Flask(__name__)
posts = {
    0 : {
        'title': 'Hello, world',
        'content': 'This is my first blog post!'
    }
}


@app.route('/')
def home():
    return 'Hello, world!'


@app.route('/post/<int:post_id>')  # /post/0 tag is flask syntax
def post(post_id):
    post = posts.get(post_id)
    if not post: # post will be null if not found
        return render_template('404.html', message=f'A post with id {post_id} was not found')
    # return f"Post : {post['title']}, content : \n\n{post['content']}"
    return render_template('post.html', post=post)


if __name__ == '__main__':
    app.run(debug=True)