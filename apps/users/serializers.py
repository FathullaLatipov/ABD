from rest_framework import serializers

from apps.users.models import Courses, HomeWork, MentorModel, StudentsModel


class CoursesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'


class HomeWorkSerializers(serializers.ModelSerializer):
    class Meta:
        model = HomeWork
        fields = '__all__'


class MentorModelSerializers(serializers.ModelSerializer):
    course_direction = CoursesSerializers()

    class Meta:
        model = MentorModel
        fields = '__all__'


class StudentsModelSerializers(serializers.ModelSerializer):
    std_direction = CoursesSerializers()
    mentor = MentorModelSerializers()

    class Meta:
        model = StudentsModel
        fields = '__all__'
