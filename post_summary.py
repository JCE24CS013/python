import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts")
posts = response.json()
counts = {}
for post in posts:
    user_id = post["userId"]
    if user_id in counts:
        counts[user_id] += 1    else:
        counts[user_id] = 1
for user_id, total_posts in counts.items():
    print("User", user_id, "wrote", total_posts, "posts")