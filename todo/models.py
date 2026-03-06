# Django에서 데이터베이스 모델을 만들기 위한 도구를 불러옴
from django.db import models


# 데이터베이스 테이블 하나 = Todo 클래스 하나
# 각 필드(컬럼) 설명
class Todo(models.Model):
    name = models.CharField(max_length=100)  # 할 일 이름 (최대 100글자, 짧은 텍스트)
    description = models.TextField(
        blank=True
    )  # 할 일 설명 (긴 텍스트, blank=True → 비워도 됨)
    complete = models.BooleanField(
        default=False
    )  # 완료 여부 (True/False, 기본값은 미완료)
    exp = models.PositiveIntegerField(default=0)  # 경험치 (양수만 가능, 기본값 0)
    completed_at = models.DateTimeField(
        null=True, blank=True
    )  # 완료한 시간 (null=True → DB에 null 허용, 완료 전엔 비어있음)
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # 생성된 시간 (처음 저장될 때 자동으로 기록, 이후 변경 불가)
    updated_at = models.DateTimeField(
        auto_now=True
    )  # 수정된 시간 (저장할 때마다 자동으로 현재 시간 갱신)

    def __str__(self):  # Django 관리자 페이지 등에서 이 객체를 이름으로 표시해줌
        return self.name  # 없으면 Todo object (1) 이런 식으로 보임
