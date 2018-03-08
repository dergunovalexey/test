from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from core.views import ToDoViewSet, Auth


router = DefaultRouter()

router.register('todos', ToDoViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', Auth.as_view({'post': 'create', 'delete': 'destroy'})),
]
