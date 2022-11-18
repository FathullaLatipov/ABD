from django.contrib import admin
from apps.diary.models import TimeTable, Diary
# Register your models here.
admin.site.register(TimeTable)
admin.site.register(Diary)
