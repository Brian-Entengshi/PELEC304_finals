from django.contrib import admin
from .models import Course, Tuition, Instructor, Semester, Student

admin.site.register(Course)
admin.site.register(Tuition)
admin.site.register(Instructor)
admin.site.register(Semester)
admin.site.register(Student)