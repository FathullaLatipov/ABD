from django.urls import path

from apps.diary.views import TimeTableView, DiaryView

urlpatterns = [
    path('time-table/', TimeTableView.as_view(), name='time-table'),
    path('diaries/', DiaryView.as_view(), name='diary'),
]