from django.contrib import admin
from .models import User, WashCompany, Washer, Service, Order


admin.site.register([User, WashCompany, Washer, Service, Order,])
