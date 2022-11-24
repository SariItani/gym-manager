from django.urls import path
from .views import index, customers, schedule, personal, cams, stock

urlpatterns = [
    path('', index, name='index'),
    path('customers/', customers, name='customers'),
    path('schedule/', schedule, name='schedule'),
    path('personal/', personal, name='personal'),
    path('cams/', cams, name='cams'),
    path('stock/', stock, name='stock'),
]
