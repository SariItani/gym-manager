from django.urls import path
from .views import index, login, signin, dashboard, programs, ux

urlpatterns = [
    path("", login, name='login'),
    path("sign-in/", signin, name='sign-in'),
    path('index/<int:userID>', index, name='index'),
    path('dashboard/<int:userID>', dashboard, name='dashbaord'),
    path('programs/<int:userID>', programs, name='programs'),
    path('ux/<int:userID>', ux, name='ux'),
]
