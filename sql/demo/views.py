from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Student, Class, GeneralGrade

# Create your views here.
def index(request):
    student_list = Student.objects.all()
    return render(request,
                  'blog/index.html',
                  context={'student_list': student_list})

def detail(request, pk):
    post = get_object_or_404(Student, pk=pk)
    return render(request,
                  'blog/detail.html',
                  context={'student': post})