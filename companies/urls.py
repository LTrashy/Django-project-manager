from django.contrib import admin
from django.urls import path, include
from .views import signup, home, companies, signout, signin

urlpatterns = [
    path('signup/', signup, name="signup"),
    path("", home, name="home"),
    path('companies/<userN>/', companies, name="companies"),
    path('logout/', signout, name="signout"),
    path("signin/", signin, name="signin")
]