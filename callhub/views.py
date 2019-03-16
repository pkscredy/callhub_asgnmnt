import time

from django.core.cache import cache
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from rest_framework.views import APIView

from callhub.constants import HOME_PAGE
from callhub.dbapi import FibSeriesDbio
from callhub.handlers.call_logic import retreive_num


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
                'cache': True
            }
            return render(request, HOME_PAGE, response)
        else:
            response = retreive_num(num)
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
