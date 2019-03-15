from rest_framework import status
from rest_framework.views import APIView
from django.core.cache import cache
from rest_framework.response import Response
from callhub.handlers.call_logic import retreive_num


class FibView(APIView):
    def get(self, request):
        num = int(request.query_params.get('num'))
        if num in cache:
            result = cache.get(num)
            response = {'num': num, 'result': result, 'cache': True}
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = retreive_num(num)
            return Response(response, status=status.HTTP_200_OK)

# 
# class FibHtmlView(APIView):
#     def get(self, request):
#         return
