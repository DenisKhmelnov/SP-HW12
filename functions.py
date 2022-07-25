import json

def main():
    print(find_posts("пос"))


def load_data():
    with open("posts.json", encoding="utf-8") as file:
        return json.load(file)


def find_posts(query):
    matched_posts = []
    all_posts = load_data()

    for post in all_posts:
        if query.lower() in post["content"].lower():
            matched_posts.append(post)

    return matched_posts


def get_pic_url(picture):
    filename = picture.filename
    pic_url = f"/uploads/images/{filename}"
    return pic_url


def save_post(picture, content):
    # сохраняем картинку
    pic_url = get_pic_url(picture)
    picture.save("." + pic_url)

    # сохраняем пост
    post_to_add = {"pic": pic_url, "content": content}
    all_posts = load_data()
    all_posts.append(post_to_add)

    with open("./posts.json", "w") as file:
        json.dump(all_posts, file,  ensure_ascii=False)