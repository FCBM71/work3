from django.contrib import admin
from .models import Profile

# 注册 Profile 模型到 Django 管理后台
admin.site.register(Profile)
