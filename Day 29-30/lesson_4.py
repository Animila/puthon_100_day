facebook_posts = [
    {"likes": 21, "Comments": 2},
    {"likes": 21, "Comments": 2, "Shares": 1},
    {"likes": 21, "Comments": 2, "Shares": 3},
    {"Comments": 21, "Shares": 2},
    {"Comments": 21, "Shares": 2},
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post["likes"]
    except KeyError as msg:
        print(f"Не найден {msg}")
        total_likes += 0

print(total_likes)