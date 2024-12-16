from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from .models import Course,Student
# Create your views here.
def  index(request: WSGIRequest):
    post=Course.objects.all()
    post2=Student.objects.all()
    context={
        "post":post ,
        "post2":post2
    }
    return render(request,'index.html',context)


def post_by_curses(request,course_id):
    post2=Student.objects.filter(course_id=course_id)
    context = {
        "post": post2,
    }
    return render(request,'index.html',context)