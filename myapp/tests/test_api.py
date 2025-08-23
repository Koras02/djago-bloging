from rest_framewort.test import APITestCase
from rest_framework import status 
from django.urls import reverse
from myapp.models import Post

class PostAPITest(APITestCase):
     def setUp(self):
         self.post = Post.objects.create(title="API 테스트", content="본문")
         self.url = reverse("post-list") # e.g. /api/posts/
         
     def test_get_post_list(self):
         response = self.client.get(self.url)
         self.assertEqual(response.status_code, status.HTTP_200_OK)
         self.assertEqual(len(response.data), 1)
         self.assertEqual(response.data[0]["title"], "API 테스트")
    
    def test_create_post(self):
        data = { "title": "새 글", "content": "새 본문 " }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)
        