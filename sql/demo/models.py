from django.db import models
from django.urls import reverse


# Create your models here.
class Student(models.Model):
    student_number = models.IntegerField(verbose_name='学生学号')
    name = models.CharField(max_length=100, verbose_name='姓名')
    gender = models.CharField(max_length=10, verbose_name='性别')
    birth_date = models.DateField(verbose_name='出生日期')
    entrance_grade1 = models.IntegerField(verbose_name='语文成绩', blank=True, null=True)
    entrance_grade2 = models.IntegerField(verbose_name='数学成绩', blank=True, null=True)
    entrance_grade3 = models.IntegerField(verbose_name='英语成绩', blank=True, null=True)
    entrance_grade4 = models.IntegerField(verbose_name='政治成绩', blank=True, null=True)
    entrance_grade5 = models.IntegerField(verbose_name='历史成绩', blank=True, null=True)

    class Meta:
        verbose_name = '学生'
        verbose_name_plural = '学生'

    def get_absolute_url(self):
        return reverse('demo:detail', kwargs={'pk': self.pk})


class Class(models.Model):
    class_number = models.IntegerField(verbose_name='课程号')
    class_name = models.CharField(max_length=100, verbose_name='课程名称')
    class_credit = models.IntegerField(verbose_name='学分')

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = '课程'

class GeneralGrade(models.Model):
    s_grade = models.IntegerField(verbose_name='成绩', blank=True, null=True)
    s_subject = models.IntegerField(verbose_name='课程号')
    s_number = models.IntegerField(verbose_name='学号')

    class Meta:
        verbose_name = '成绩'
        verbose_name_plural = '成绩'