from flask import Blueprint, render_template,request
from app.post.dao.post_dao import PostDAO,DATA_PATH
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route("/")
def page_index():
    posts = PostDAO(DATA_PATH)
    post = posts.load_data()
    return render_template('index.html', posts= post)

@main_blueprint.route("/users/<username>")
def user_feed_page(username):
    posts = PostDAO(DATA_PATH)
    post = posts.get_posts_all(username)
    return render_template('user-feed.html' , userpost = post)