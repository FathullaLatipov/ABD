from django.contrib import admin
from apps.users.models import Courses, HomeWork, MentorModel, StudentsModel
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    # fields = ('username', 'tel') #Вывести нужное поле
    # exclude = ('username',) #Исключить поле 
    list_display = ('username', 'email', 'course_direction')
    search_fields = ('username', 'email')
    ordering = ('username',)
    list_per_page = 10
    
admin.site.register(Courses)
admin.site.register(HomeWork)
admin.site.register(MentorModel, UserAdmin)
admin.site.register(StudentsModel)