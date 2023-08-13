class User:
    def __init__(self, name):
        self.name = name
        self.followers = []
        self.posts = []

    def follow(self, observer):
        self.followers.append(observer)

    def unfollow(self, observer):
        self.followers.remove(observer)

    def notify_followers(self, post):
        for follower in self.followers:
            follower.update(self.name, post)

    def post_update(self, post_content):
        post = {"content": post_content}
        self.posts.append(post)
        self.notify_followers(post_content)


class Follower:
    def update(self, username, post):
        print(f"{username} posted a new update: {post}")

# Creating users
alice = User("Alice")
bob = Follower() # Bob is a follower who wants to observe Alice

# Alice followed by Bob
alice.follow(bob)

# Alice posts an update
alice.post_update("I love learning design patterns!")

# Output:
# Alice posted a new update: I love learning design patterns!
