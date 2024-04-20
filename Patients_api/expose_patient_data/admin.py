from django.contrib import admin
from .models import Patient, Laboratorytest, Medical, Orderdetail, Testorder, Testresult

# Register your models here.
admin.site.register(Patient)
admin.site.register(Laboratorytest)
admin.site.register(Medical)
admin.site.register(Orderdetail)
admin.site.register(Testorder)
admin.site.register(Testresult)
