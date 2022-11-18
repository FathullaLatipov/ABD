from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from apps.users.models import Courses, HomeWork, MentorModel, StudentsModel
from apps.users.serializers import CoursesSerializers, HomeWorkSerializers, MentorModelSerializers, \
    StudentsModelSerializers


class CourseViews(generics.ListAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializers


class HomeWorkView(generics.ListAPIView):
    queryset = HomeWork.objects.all()
    serializer_class = HomeWorkSerializers


class MentorView(generics.ListAPIView):
    queryset = MentorModel.objects.all()
    serializer_class = MentorModelSerializers


class StudentView(generics.ListAPIView):
    queryset = StudentsModel.objects.all()
    serializer_class = StudentsModelSerializers
