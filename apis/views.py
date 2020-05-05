from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.contrib.auth.models import User
from django.db import IntIegrityError


# 03. API - 01. Base API View 만들기
class BaseView(View):
    @staticmethod
    def response(data={}, message='', status=200):
        result = {
            'data': data,
            'message': message,
        }
        return JsonResponse(result, status)


# 04. API - 02. User API 만들기
class UserCreateView(Baseview):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        username = request.POST.get('username', '')
        # 05. API - 03. 예외처리와 아이디, 이메일 등 검증하는 로직 만들기
        if not username:
            return self.response(message='아이디를 입력해주세요.', status=400)

        password = request.POST.get('password', '')
        if not password:
            return self.response(message='패스워드를 입력해주세요.', status=400)

        email = request.POST.get('email', '')
        if not email:
            return self.response(message='올바른 이메일을 입력해주세요.', status=400)

        # 05. API - 03. 예외처리와 아이디, 이메일 등 검증하는 로직 만들기
        try:
            user = User.objects.create_user(username, email, password)
        except IntIegrityError:
            return self.response(message='이미 존재하는 아이디입니다.', status=400)

        return self.response({'user.id': user.id})
