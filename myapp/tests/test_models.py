from django.test import TestCase
from myapp.models import Post

class PostModelTest(TestCase):
    def test_short_title_returns_first_10_chars(self):
         post = Post.objects.create(title="Django Unit Test!", content="...")
         self.assertEqual(post.short_title(), "Django Uni")