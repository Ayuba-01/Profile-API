from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HelloApiView, HelloViewSet, UserProfileViewSet

router = DefaultRouter()
router.register(r"hello-viewset", HelloViewSet, basename="hello-viewset")
router.register(r"profile", UserProfileViewSet)

urlpatterns = [
    path("greeting-view/", HelloApiView.as_view()),
    path("", include(router.urls))
]

