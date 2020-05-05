from django.http import JsonResponse
from django.views import View


# 03. API - 01. Base API View 만들기
class BaseView(View):
    @staticmethod
    def response(data={}, message='', status=200):
        result = {
            'data': data,
            'message': message,
        }
        return JsonResponse(result, status)
