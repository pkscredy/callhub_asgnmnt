from callhub.models import FibSeries
from base.dbapi import AbstractBaseDbIO
from django_redis import get_redis_connection
# from callhub.handlers.call_logic import cache_dec


class FibSeriesDbio(AbstractBaseDbIO):

    @property
    def model(self):
        return FibSeries

    @staticmethod
    def tear_down():
        get_redis_connection("default").flushall()
