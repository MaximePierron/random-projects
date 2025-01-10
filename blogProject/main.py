from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
data = response.json()
blog_posts = []
for post in data:
    blog_post = Post(post["id"], post["title"], post["subtitle"], post["body"])
    blog_posts.append(blog_post)


@app.route('/')
def home():
    return render_template("index.html", blog_posts=blog_posts)


@app.route('/post/<int:post_id>')
def get_post(post_id):
    blog_post_to_print = [post_dict for post_dict in blog_posts if post_dict.id == post_id][0]
    return render_template("post.html", blog_post=blog_post_to_print)


if __name__ == "__main__":
    app.run(debug=True)
