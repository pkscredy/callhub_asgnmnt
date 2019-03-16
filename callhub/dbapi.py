from django_redis import get_redis_connection

from base.dbapi import AbstractBaseDbIO
from callhub.models import FibSeries


class FibSeriesDbio(AbstractBaseDbIO):

    @property
    def model(self):
        return FibSeries

    @staticmethod
    def tear_down():
        get_redis_connection("default").flushall()
