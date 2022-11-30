from django.urls import path
from .views import index, customers, schedule, personal, cams, stock, create

urlpatterns = [
    path('', index, name='index'),
    path('customers/', customers, name='customers'),
    path('create/', create, name='create'),
    path('schedule/', schedule, name='schedule'),
    path('personal/', personal, name='personal'),
    path('cams/', cams, name='cams'),
    path('stock/', stock, name='stock'),
]
