from core.post.models import Post
from core.user.models import User
user = User.objects.first()

user

data = {"author": user, "body":"A simple test"}
post = Post.objects.create(**data)

post

post.author

user.post_set.all()