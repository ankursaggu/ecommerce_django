from django.contrib import admin
from django.urls import path, include

#from ecommerce.ecommerce import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),  # Include URLs from the store app
]
