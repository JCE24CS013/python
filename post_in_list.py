import requests
def get_user_posts(user_id):
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"
    )
    posts = response.json()
    return posts
user_posts = get_user_posts(1)
print(user_posts)