from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('create/', views.create_student, name='create_student'),
    path('student/<int:id>/update', views.update_student, name='update_student'),
    path('student/<int:id>/delete', views.delete_student, name='delete_student')

]