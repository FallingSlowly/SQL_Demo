from django.contrib import admin
from .models import GeneralGrade, Student, Class

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_number', 'name', 'gender', 'birth_date',
                    'entrance_grade1', 'entrance_grade2', 'entrance_grade3',
                    'entrance_grade4', 'entrance_grade5']

class ClassAdmin(admin.ModelAdmin):
    list_display = ['class_number', 'class_name', 'class_credit']

class GradeAdmin(admin.ModelAdmin):
    list_display = ['s_number', 's_subject', 's_grade']

admin.site.register(GeneralGrade, GradeAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Class, ClassAdmin)