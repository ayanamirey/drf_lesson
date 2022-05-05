from django.contrib import admin
from django.urls import path, include
from women.views import WomenAPIList, WomenAPIUpdate, WomenAPIDestroy
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'women', WomenViewSet, basename='women')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/women/', WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/', WomenAPIDestroy.as_view()),
    # path('api/v1/', include(router.urls))
]
