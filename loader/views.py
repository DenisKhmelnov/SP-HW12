import logging
from flask import Blueprint, render_template, request
from functions import save_post, get_pic_url

loader_blueprint=Blueprint('loader', __name__, template_folder="templates")


@loader_blueprint.get("/post")
def page_post_form():
    return render_template("post_form.html")


@loader_blueprint.post("/post")
def page_save_post():
    picture = request.files.get("picture")
    content = request.form.get("content")

    if not picture or not content:
        return "Нет картинки или контента"
    if picture.filename.split(".")[-1] not in ["jpg", "jpeg", "png"]:
        logging.info("Файл не является картинкой")
        return "Неверный формат файла"

    save_post(picture, content)

    return render_template("post_uploaded.html", pic_url=get_pic_url(picture), content=content)
