from django.urls import path
from .views.templates_views import TodoListView
from .views.api_views import TodoListAPI


app_name = "todo"

urlpatterns = [
    # path("list/", views.todo_list, name="todo_List"), # 첫 테스트용
    path("list/", TodoListView.as_view(), name="list"),
    # api
    path("api/list/", TodoListAPI.as_view(), name="todo_api_list"),
]
