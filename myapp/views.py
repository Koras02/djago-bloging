from django.shortcuts import render
from .models import Product

# Create your views here.
def product_list(request):
    # 쿼리 셋을 사용하여 필터링할 가격을 가져옴
    min_price = request.GET.get('min_price', 0)
    max_price = request.GET.get('max_price', 10000)
    
    # 가격 범위에 따른 제품 필터링
    products = Product.objects.filter(price__gte=min_price, price__lte=max_price) 
    
    # 제품 목록을 템플릿에 전달
   
    return render(request, 'myapp/product_list.html', {'products': products})

def example_view(request):
    # 예시 뷰 함수 
    context = {
        "title": "Template Example",
        'heading': "Django Template Testing",
        "description": "This is a simple example of a Django template.",
        "items": ["Keyboard", "Mouse", "Monitor", "CPU"],
    }
    return render (request, "myapp/example.html", context)


def index(request):
      return render(request, "index.html");
  
