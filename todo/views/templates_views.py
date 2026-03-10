# Create your views here.
# HTML 템플릿을 화면에 보여주는 함수
# 같은 앱의 models.py 에서 Todo 모델 가져오기
# DB에서 데이터를 꺼내오려면 필요
# 지금 당장 사용은 안 하지만 나중에 클래스형 뷰 쓸 때 필요해서 미리 import

from django.shortcuts import render
from ..models import Todo
from django.urls import reverse_lazy
from django.views.generic import ListView

# 지금 당장 사용은 안 하지만 나중에 클래스형 뷰 쓸 때 필요해서 미리 import


def todo_list(request):  #  함수형
    todos = Todo.objects.all()
    return render(request, "todo/todo.html", {"todos": todos})


# 목록 조회
class TodoListView(ListView):
    model = Todo  # 이 뷰가 사용할 모델 지정 (Todo 테이블 데이터를 조회)

    template_name = "todo/list.html"
    # 데이터를 보여줄 HTML 템플릿 파일 지정

    context_object_name = "todos"
    # 템플릿에서 사용할 변수 이름 (기본값 object_list 대신 todos 사용)

    ordering = ["-created_at"]
    # 데이터 정렬 방식 (created_at 기준 내림차순 → 최신 글이 먼저)

    success_url = reverse_lazy("todo:list")
    # 작업 성공 후 이동할 URL (ListView에서는 보통 사용하지 않지만 설정 가능)
