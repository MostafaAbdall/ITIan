from django.urls import path
from trainees import views

urlpatterns = [
    path('', views.trainees_list, name='trainees_list'),
    path('add/', views.add_trainee, name='add_trainee'),
    path('update/<int:id>/', views.update_trainee, name='update_trainee'),
    path('delete/<int:id>/', views.delete_trainee, name='delete_trainee'),

] 