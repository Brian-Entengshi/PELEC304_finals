from django.urls import path
from . import views

urlpatterns = [
    path('course/', views.course, name="course"),
    path('tuition/', views.tuition, name="tuition"),
    path('instructor/', views.instructor, name="instructor"),
    path('semester/', views.semester, name="semester"),
    path('student/', views.student, name="student"),
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.add_students, name='add_students'),
    path('course/add/', views.add_course, name='add_course'),
    path('tuition/add/', views.add_tuition, name='add_tuition'),
    path('instructor/add/', views.add_instructor, name='add_instructor'),
    path('semester/add/', views.add_semester, name='add_semester')
]
