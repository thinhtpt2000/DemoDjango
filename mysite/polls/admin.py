from django.contrib import admin
from .models import Choice, Question

# Register your models here.
# Đăng kí các models ở đây

admin.site.register(Question)
admin.site.register(Choice)