from django.contrib import admin
from django.urls import path, include
#from reviews.views import ProductViewSet, ImageViewSet
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
#router.register(r'product', ProductViewSet, basename='Product')
#router.register(r'image', ImageViewSet, basename='Image')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('authapi.urls')),
    path('', include(router.urls)),
]