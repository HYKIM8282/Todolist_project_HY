# URL 경로를 등록하는 path 함수 불러오기
# . = 현재 폴더(todo 앱) 를 의미
# 같은 폴더에 있는 views.py 를 불러오기

from django.urls import path
from . import views

# 이 URL들이 todo 앱 소속임을 선언
# 나중에 URL을 이름으로 부를 때 todo:list 형태로 사용 가능

app_name = "todo"

# | 부분 | 의미 |
# | `"list/"` | URL 주소 |
# | `views.todo_list` | 이 URL로 오면 실행할 함수 |
# | `name="list"` | 이 URL의 별명 |

urlpatterns = [
    # path("list/", views.todo_list, name="list"),  # 첫 테스트용
    path("list/", views.TodoListView.as_view(), name="list"),  # 실제 작동용 list
]

### 전체 흐름
# 브라우저에서 접속 http://127.0.0.1:8000/todo/list/
# mysite/urls.py 에서 "todo/" 확인
# todo/urls.py 에서 "list/" 확인
# views.todo_list 함수 실행
# 화면에 결과 출력
