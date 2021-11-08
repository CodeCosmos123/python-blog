from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

blog_api_url = "https://api.npoint.io/4af156202f984d3464c3"
blog_api_response = requests.get(blog_api_url)
blog_api_data = blog_api_response.json()

blog_post_objects = [Post(blog["id"], blog["title"], blog["subtitle"], blog["body"]) for blog in blog_api_data]

@app.route("/")
def render_home_page():
    return render_template("index.html", blogs=blog_post_objects)

@app.route("/post/<int:blog_id>")
def render_blog_post_page(blog_id):
    for blog in blog_post_objects:
        if blog.id == blog_id:
            goal_blog = blog 
    return render_template("post.html", blog=goal_blog)

if __name__ == "__main__":
    app.run()
