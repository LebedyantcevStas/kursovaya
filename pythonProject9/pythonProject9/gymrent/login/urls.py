from django.urls import path
from .views import LogoutView, CreateAccountView,LoginView


app_name = 'login'

urlpatterns = [
    path('', LoginView.as_view()),
    path('', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('create/', CreateAccountView.as_view(), name="create"),
]