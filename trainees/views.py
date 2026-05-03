from django.shortcuts import render

# Create your views here.
def trainees_list(request):
    return render(request, 'trainees/trainee_list.html', { 
        'trainees': ["ahmed", "mohamed", "sara"] 
    })

def add_trainee(request):
    return render(request, 'trainees/add_trainee.html')

def update_trainee(request, id):
    return render(request, 'trainees/update_trainee.html', { 
        'id': id
    })

def delete_trainee(request, id):
    return render(request, 'trainees/delete_trainee.html', { 
        'id': id
    })