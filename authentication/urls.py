from django.urls import include, path
from django.views.generic import TemplateView
from authentication.views import CreateUser, LoginUser, LogoutUser
from authentication.views import GetUserByID


urlpatterns = [
    path("signup/", CreateUser.as_view(), name="signup"),
    path("login/", LoginUser.as_view(), name="login"),
    path("logout/", LogoutUser.as_view(), name="logout"),
    path("user/<str:pk>/profile/", GetUserByID.as_view(), name="user/profile"),
    # path('swagger/', include('authentication.swagger')),

]