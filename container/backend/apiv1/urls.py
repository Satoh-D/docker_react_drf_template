from django.urls import path, include
from rest_framework import routers

# views
from . import views

router = routers.DefaultRouter()

# ルーティング追加
urlpatterns = [
    path('', include(router.urls)),
]

