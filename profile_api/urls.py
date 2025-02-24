from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HelloApiView, HelloViewSet, UserProfileViewSet, UserLoginApiView, ProfileFeedItemViewSet

router = DefaultRouter()
router.register(r"hello-viewset", HelloViewSet, basename="hello-viewset")
router.register(r"profile", UserProfileViewSet)
router.register(r"feeds", ProfileFeedItemViewSet)

urlpatterns = [
    path("greeting-view/", HelloApiView.as_view()),
    path("login/", UserLoginApiView.as_view()),
    path("", include(router.urls))
]

