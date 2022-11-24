from django.contrib import admin
from .models import Schedule, Workers, Customers, Cams, Stock

# Register your models here.
admin.site.register(Schedule)
admin.site.register(Workers)
admin.site.register(Customers)
admin.site.register(Cams)
admin.site.register(Stock)
