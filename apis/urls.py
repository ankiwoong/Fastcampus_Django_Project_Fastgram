from django.urls import path

from apis.views import UserCreateView


urlpatterms = [
    # 05. API - 03. 예외처리와 아이디, 이메일 등 검증하는 로직 만들기
    path('v1/users/create', UserCreateView.as_view(), name='apis_v1_user')
]
