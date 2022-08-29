from rest_framework import routers
from django.urls import path, include
from .views import BoardViewSet, TasksViewSet, index


router = routers.DefaultRouter()
router.register(r'boards', BoardViewSet)
router.register(r'tasks', TasksViewSet)


urlpatterns = [
    path('', index, name="homepage"),
    path('api/', include(router.urls))
]
