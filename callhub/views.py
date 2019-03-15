# from rest_framework import status
from rest_framework.views import APIView
from django.core.cache import cache
# from rest_framework.response import Response
from callhub.handlers.call_logic import retreive_num
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from callhub.dbapi import FibSeriesDbio


class FibView(APIView):

    def get(self, request, num):
        num = int(num)
        if num in cache:
            result = cache.get(num)
            response = {'num': num, 'result': result, 'cache': True}
            # return Response(response, status=status.HTTP_200_OK)
            return render(request, 'fibseries.html', response)
        else:
            response = retreive_num(num)
            # return Response(response, status=status.HTTP_200_OK)
            return render(request, 'fibseries.html', response)


class ClearCacheView(APIView):
    def delete(self, request):
        FibSeriesDbio().tear_down()


class FibHtmlView(APIView):
    def get(self, request):
        context = {}
        return render(request, 'fibseries.html', context)

    def post(self, request):
        fib_num = request.data.dict().get('fibNo')
        arg_num = reverse('fib_num', args=(fib_num,))
        return HttpResponseRedirect(arg_num)
