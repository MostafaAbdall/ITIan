from django.shortcuts import render

from courses.models import Course

# Create your views here.
def courses_list(request):
    context ={ "courses": Course.objects.all() }
    return render(request, 'courses/courses_list.html', context)
def add_course(request):
    return render(request, 'courses/add_course.html')

def update_course(request, id):
    return render(request, 'courses/update_course.html', { 
        'id': id
    })

def delete_course(request, id):
    return render(request, 'courses/delete_course.html', { 
        'id': id
    })