# Create your views here.
# HTML 템플릿을 화면에 보여주는 함수
# 같은 앱의 models.py 에서 Todo 모델 가져오기
# DB에서 데이터를 꺼내오려면 필요
# 지금 당장 사용은 안 하지만 나중에 클래스형 뷰 쓸 때 필요해서 미리 import

from django.shortcuts import render
from .models import Todo

# 지금 당장 사용은 안 하지만 나중에 클래스형 뷰 쓸 때 필요해서 미리 import


def todo_list(request):  #  함수형
    todos = Todo.objects.all()
    return render(request, "todo/todo.html", {"todos": todos})
