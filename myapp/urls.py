from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
       path('example/', views.example_view, name= "example"),
       # 예시: 제품 목록 페이지 연결
       path('products/', views.product_list, name="product_list"),
       path('admin/', admin.site.urls),
       path('', views.index, name="index"),
]