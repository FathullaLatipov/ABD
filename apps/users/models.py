from django.db import models

# Create your models here.

class Courses(models.Model):
    COURSE_CHOICES = (
        ('Software Engineer', 'Software Engineer'),
        ('Data Science', 'Data Science'),
        ('Full-Stack', 'Full-Stack'),
    )
    courses = models.CharField(choices=COURSE_CHOICES, default='Software Engineer', max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.courses
    
    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
   
        
class HomeWork(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    comment = models.TextField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Домашнее задание"
        verbose_name_plural = "Домашние задания"
        
        
class MentorModel(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    date_of_birth = models.DateTimeField()
    age = models.IntegerField()
    birth_place = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    course_direction = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='direction')

    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name = "Ментор"
        verbose_name_plural = "Менторы"
        
         
class StudentsModel(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    date_of_birth = models.DateTimeField()
    age = models.IntegerField()
    birth_place = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    std_direction = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='std_course')
    astro_purchase = models.CharField(max_length=255)
    mentor = models.ForeignKey(MentorModel, on_delete=models.CASCADE, related_name='std_mentor')

    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
        