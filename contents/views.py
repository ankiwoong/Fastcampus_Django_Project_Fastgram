from django.shortcuts import render
from django.views.generic.base import TemplateView


# 06. API - 05. 로그인 테스트 해볼 수 있는 페이지 만들기
class HomeView(TemplateView):
    template_name = 'home.html'
