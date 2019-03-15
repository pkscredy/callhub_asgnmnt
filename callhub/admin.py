from django.contrib import admin

from callhub.models import FibSeries


@admin.register(FibSeries)
class SeriesModelAdmin(admin.ModelAdmin):
    list_display = ('num_key', 'result', 'exec_time')
    search_fields = ('num_key',)
