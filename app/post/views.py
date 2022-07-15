import json
import logging

from flask import Blueprint, render_template,request, jsonify
from app.comment.dao.comment_dao import CommentDAO, COMMENT_PATH
from app.post.dao.post_dao import PostDAO,DATA_PATH


post_blueprint = Blueprint('post_blueprint', __name__, template_folder='templates')


@post_blueprint.route("/posts/<int:postid>")
def post_page(postid):
    posts = PostDAO(DATA_PATH)
    post = posts.get_post_by_pk(postid)
    comment = CommentDAO(COMMENT_PATH)
    result_comment = comment.get_comments_by_post_id(postid)
    return render_template('post.html', result_comment= result_comment, post = post)


@post_blueprint.route("/search",methods = ['GET'])
def post_find():
    s = request.args.get('s')
    posts_data = PostDAO(DATA_PATH)
    posts = posts_data.search_for_posts(s)
    return render_template('search.html', posts=posts)

logging.basicConfig(filename="./api.log", level=logging.INFO)
loger_api = logging.getLogger()

file_handler = logging.FileHandler("api.log")
loger_api.addHandler(file_handler)

console_handler = logging.StreamHandler()
formatter_one = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
console_handler.setFormatter(loger_api)



@post_blueprint.route('/api/posts')
def api_posts_page():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        post_data = json.load(f)
    return jsonify(post_data)

@post_blueprint.route('/api/posts/<int:post_id>')
def api_postsid_page(post_id):
    logging.info("Запрос всех книг")
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        post_data = json.load(f)
        posts = []
        for post in post_data:
            if post["pk"] == post_id:
                posts.append(post)
                logging.info("Запрос всех книг")
    return jsonify(posts)


