# from rest_framework import status
import time
from rest_framework.views import APIView
from django.core.cache import cache
# from rest_framework.response import Response
from callhub.handlers.call_logic import retreive_num
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from callhub.dbapi import FibSeriesDbio
from callhub.constants import HOME_PAGE


class FibView(APIView):

    def get(self, request, num):
        num = int(num)
        if num in cache:
            time_start = time.time()
            result = cache.get(num)
            response = {
                'num': num,
                'result': result,
                'cache_time': time.time()-time_start,
                'cache': True}
            # return Response(response, status=status.HTTP_200_OK)
            return render(request, HOME_PAGE, response)
        else:
            response = retreive_num(num)
            # return Response(response, status=status.HTTP_200_OK)
            return render(request, HOME_PAGE, response)


class FibHtmlView(APIView):
    def get(self, request):
        return render(request, HOME_PAGE)

    def post(self, request):
        fib_num = request.data.dict().get('fibno')
        arg_num = reverse('fib_num', args=(fib_num,))
        return HttpResponseRedirect(arg_num)


class ClearCacheView(APIView):
    def get(self, request):
        FibSeriesDbio().tear_down()
        return render(request, HOME_PAGE)
