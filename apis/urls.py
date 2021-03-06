from django.urls import path

from apis.views import UserCreateView, UserLoginView, UserLogoutView


urlpatterns = [
    # 05. API - 03. 예외처리와 아이디, 이메일 등 검증하는 로직 만들기
    path('v1/users/create/', UserCreateView.as_view(), name='apis_v1_user_create'),
    # 06. API - 04. 유저 로그인 API
    path('v1/users/login/', UserLoginView.as_view(), name='apis_v1_user_login'),
    # 07. API - 06. 유저 로그아웃 API
    path('v1/users/logout/', UserLogoutView.as_view(), name='apis_v1_user_logout'),
]
