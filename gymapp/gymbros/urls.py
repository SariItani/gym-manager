from django.urls import path
from .views import index, login, signin, create, dashboard, programs, ux

urlpatterns = [
    path("", login, name='login'),
    path("signin/", signin, name='signin'),
    path("create/", create, name='create'),
    path('index/', index, name='index'),
    path('dashboard/', dashboard, name='dashbaord'),
    path('programs/', programs, name='programs'),
    path('ux/', ux, name='ux'),
]
