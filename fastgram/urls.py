"""fastgram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from contents.views import HomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    # 05. API - 03. 예외처리와 아이디, 이메일 등 검증하는 로직 만들기
    path('apis/', include('apis.urls')),
    # 06. API - 05. 로그인 테스트 해볼 수 있는 페이지 만들기
    path('login_test', HomeView.as_view(), name='contents_home'),
]
