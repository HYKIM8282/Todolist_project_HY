from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Todo  # 경로변경
from ..serializers import TodoSerializer  # 경로변경


# 전체보기
class TodoListAPI(APIView):
    def get(self, request):
        # GET 요청이 들어오면 실행되는 함수

        todos = Todo.objects.all()
        # Todo 모델의 모든 데이터 조회 (QuerySet)

        serializer = TodoSerializer(todos, many=True)
        # 조회한 Todo 객체들을 Serializer로 JSON 변환 준비
        # many=True → 여러 개의 객체를 변환한다는 의미

        return Response(serializer.data)
        # serializer.data를 JSON 형태로 변환하여 API 응답으로 반환
