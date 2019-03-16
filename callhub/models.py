from django.db import models

from base.models import AbstractAuditModel


class FibSeries(AbstractAuditModel):
    num_key = models.CharField(max_length=200, blank=True, null=True)
    result = models.CharField(max_length=2000, blank=True, null=True)
    exec_time = models.CharField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return '%s ' % (self.num_key)
