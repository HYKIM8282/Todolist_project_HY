# Register your models here.
# 가장 기본 등록 방식
# Admin 옵션 커스터마이징 없음
# 그냥 기본 관리자 화면으로 등록됨
#
#
from django.contrib import admin
from .models import Todo

admin.site.register(Todo)
