from django.urls import path
from .views import Log_in, Log_out, Register, Info, UpdateUserInfo


urlpatterns = [
    path("info/", Info.as_view()),
    path("register/", Register.as_view()),
    path("logout/", Log_out.as_view()),
    path("login/", Log_in.as_view()),
    path('update/', UpdateUserInfo.as_view(), name='update-user-info'),
]