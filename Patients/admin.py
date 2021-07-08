from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Relationship)
admin.site.register(Hospital)
admin.site.register(Category)
admin.site.register(Patient)
admin.site.register(Message)
