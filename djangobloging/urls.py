from django.urls import path
from django.contrib import admin
from django.views.generic import RedirectView
from myapp.views import product_list

urlpatterns = [
    path('', RedirectView.as_view(url='/products/')),
    path('admin/', admin.site.urls),
    path('products/', product_list, name='product_list')
]
