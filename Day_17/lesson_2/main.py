class User:
    def __init__(self, user_id, username):
        print('new user being created...')
        self.id = user_id
        self.username = username
        self.follower = 0


user1 = User('001', 'Misha')
user2 = User('002', 'Jack')
print(user1.follower)