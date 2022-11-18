from django.db import models
from apps.users.models import StudentsModel, MentorModel
# Create your models here.

class TimeTable(models.Model):
    lesson = models.ForeignKey(MentorModel, on_delete=models.CASCADE, related_name='mentor_lessons')
    DAY_CHOICES = (
        ('Понедельник','Понедельник'),
        ('Вторник','Вторник'),
        ('Среда','Среда'),
        ('Четверг','Четверг'),
        ('Пятница','Пятница'),
        ('Суббота','Суббота'),
        ('Воскресенье','Воскресенье'),
    )
    days = models.CharField(choices=DAY_CHOICES, default='Понедельник', max_length=255)
    start = models.DateTimeField()
    end = models.DateTimeField()
    
    def __str__(self):
        return self.days
    
    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписания"
        
        
class Diary(models.Model):
    title = models.CharField(max_length=255)
    students = models.ForeignKey(StudentsModel, on_delete=models.CASCADE, related_name='student_book')
    mentors = models.ForeignKey(MentorModel, on_delete=models.CASCADE, related_name='mentor_book')
    schedule = models.ForeignKey(TimeTable, on_delete=models.CASCADE, related_name='time_table')
    peer_to_peer = models.ForeignKey(StudentsModel, on_delete=models.CASCADE, related_name='str_pr')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Дневник"
        verbose_name = "Дневники"
        