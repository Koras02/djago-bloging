from django.urls import path
from django.contrib import admin
from django.urls import include
# from django.views.generic import RedirectView
# from myapp.views import product_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', include('myapp.urls'))
    # path('', RedirectView.as_view(url='/products/')),
    # path('products/', product_list, name='product_list'),
]
