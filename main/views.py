from flask import Blueprint, render_template, request
from functions import find_posts
from json import JSONDecodeError

main_blueprint=Blueprint('main_blueprint', __name__, template_folder="templates")

@main_blueprint.get("/")
def main_page():
    return render_template("index.html")

@main_blueprint.get("/search/")
def show_posts():
    query = request.args.get("s")
    try:
        matched_posts = find_posts(query)
    except FileNotFoundError:
        return "Файл с данными не найден"
    except JSONDecodeError:
        return "Файл поврежден"
    return render_template("post_list.html", matched_posts=matched_posts, query=query)