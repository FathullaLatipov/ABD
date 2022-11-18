from django.urls import path

from apps.diary.views import TimeTableView, DiaryView
from apps.users.views import CourseViews, HomeWorkView, MentorView, StudentView

urlpatterns = [
    path('courses/', CourseViews.as_view(), name='courses'),
    path('homeworks/', HomeWorkView.as_view(), name='homeworks'),
    path('mentors/', MentorView.as_view(), name='mentors'),
    path('students/', StudentView.as_view(), name='students'),
]