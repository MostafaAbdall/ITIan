from django.shortcuts import render

# Create your views here.
def courses_list(request):
    return render(request, 'courses/courses_list.html', { 
        'courses': ["python", "django", "javascript"] 
    })
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