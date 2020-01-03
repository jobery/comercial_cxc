from django.contrib import admin

from apps.cxc.models import Cliente,Cargo,Abono
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Cargo)
admin.site.register(Abono)