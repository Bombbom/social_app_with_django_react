from core.comment.models import Comment 
from core.post.models import Post 
from core.user.models import User 

user = User.objects.first() 
post = Post.objects.first() 
comment_data = {"post": post, "author": user, "body": "A comment."}
comment = Comment.objects.create(**comment_data)
comment
comment.body
