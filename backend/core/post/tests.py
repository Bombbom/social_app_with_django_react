from django.test import TestCase
import pytest 

# Create your tests here.

from core.fixtures.user import user 
from core.post.models import Post 
@pytest.mark.django_db
def test_create_post(user):
    post = Post.objects.create(author=user, body="Test Post Body")
    assert post.body == "Test Post Body"
    assert post.author == user