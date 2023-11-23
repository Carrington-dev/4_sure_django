from django.contrib import admin
from django.urls import path, include
from account import views as authenicate_service
from client import views as client_service
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('register', authenicate_service.UserCreateViewSet, basename="register")


router = DefaultRouter()
router.register('clients', client_service.ClientViewSet, basename="client")
# router.register('login', authenicate_service.UserVerifyViewSet, basename="login")

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", authenicate_service.home, name="home"),
    # path("register", authenicate_service.register, name="register"),
    path("", include(router.urls)),
    # path("", include(client_router.urls)),
    path("login", authenicate_service.login, name="login"),
]
