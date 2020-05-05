from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# 06. API - 05. 로그인 테스트 해볼 수 있는 페이지 만들기
# 08. API - 07. 로그인 페이지 분리
class HomeView(TemplateView):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(HomeView, self).dispatch(request, *args, **kwargs)

    template_name = 'home.html'
