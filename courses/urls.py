from django.urls import path
from courses import views

urlpatterns = [
    path('', views.courses_list, name='courses_list'),
    path('add/', views.add_course, name='add_course'),
    path('update/<int:id>/', views.update_course, name='update_course'),
    path('delete/<int:id>/', views.delete_course, name='delete_course'),

] 