from django import forms
from .models import Course, Tuition, Instructor, Semester, Student

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'instructor_name', 'start_date', 'end_date', 'course_id']

class TuitionForm(forms.ModelForm):
    class Meta:
        model = Tuition
        fields = ['payment_id', 'student_id', 'amount', 'payment_date', 'payment_status']

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['instructor_id', 'name', 'email', 'contact_number', 'courses_taught']

class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ['semester_id', 'semester_name', 'start_date', 'end_date', 'status_status']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'password', 'email', 'birthdate', 'age']