import json

def main():
    print(find_posts("пос"))


def load_data():
    with open("posts.json") as file:
        return json.loads(file.read())


def find_posts(query):
    matched_posts = []
    all_posts = load_data()

    for post in all_posts:
        if query in post["content"]:
            matched_posts.append(post)

    return matched_posts
