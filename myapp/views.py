
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Post


def index(request):
    return HttpResponse("Hello, this is index page")

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post", post})