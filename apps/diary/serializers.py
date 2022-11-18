from rest_framework import serializers

from apps.diary.models import TimeTable, Diary
from apps.users.models import MentorModel, StudentsModel


class MentorsModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = MentorModel
        fields = '__all__'


class TimeTableSerializers(serializers.ModelSerializer):
    lesson = MentorsModelSerializers()

    class Meta:
        model = TimeTable
        fields = '__all__'


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentsModel
        fields = '__all__'


class PeerToPeerSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentsModel
        fields = '__all__'


class DiarySerializer(serializers.ModelSerializer):
    students = StudentSerializers()
    mentors = MentorsModelSerializers()
    schedule = TimeTableSerializers()
    peer_to_peer = PeerToPeerSerializers()

    class Meta:
        model = Diary
        fields = '__all__'
