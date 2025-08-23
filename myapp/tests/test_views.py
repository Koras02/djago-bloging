from django.test import TestCase
from django.urls import reverse
from myapp.models import Post

class PostViewTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title="테스트 제목", content="테스트용 본문입니다")
        
    def test_post_detail_view_success(self):
        url = reverse("post_detail", args=[self.post.pk])
        response = self.client.get(url)
        
        # HTTP 상태 코드 확인
        self.assertEqual(response.status_code, 200)
        
        # 템플릿 사용 확인
        self.assertTemplateUsed(response, "myapp/post_detail.html")
        
        # 컨텍스트 데이터 확인
        self.assertContains(response, "테스트 제목")
        self.assertContains(response, "테스트 본문")
        
    def test_post_detail_view_not_found(self):
        url = reverse("post_detail", args=[9999]) # 없는 글 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        