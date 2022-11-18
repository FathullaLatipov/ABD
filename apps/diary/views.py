from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from apps.diary.models import TimeTable, Diary
from apps.diary.serializers import TimeTableSerializers, DiarySerializer


class TimeTableView(generics.ListAPIView):
    queryset = TimeTable.objects.all()
    serializer_class = TimeTableSerializers


class DiaryView(generics.ListAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
