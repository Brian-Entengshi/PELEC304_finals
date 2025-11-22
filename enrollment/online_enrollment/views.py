from django.shortcuts import render, redirect
from .models import Course, Tuition, Instructor, Semester, Student
from .forms import CourseForm, TuitionForm, InstructorForm, SemesterForm, StudentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def course(request):
    courses = Course.objects.all()
    return render(request, 'course.html', {'courses': courses})

@login_required(login_url='login')
def tuition(request):
    tuitions = Tuition.objects.all()
    return render(request, 'tuition.html', {'tuitions': tuitions})

@login_required(login_url='login')
def instructor(request):
    instructors = Instructor.objects.all()
    return render(request, 'instructor.html', {'instructors': instructors})

@login_required(login_url='login')
def semester(request):
    semesters = Semester.objects.all()
    return render(request, 'semester.html', {'semesters': semesters})

@login_required(login_url='login')
def student(request):
    students = Student.objects.all()
    return render(request, 'student.html', {'students': students})

@login_required(login_url='login')
def add_students(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully!')
            return redirect('studentslist')
    else:
        form = StudentForm()
    return render(request, 'add_students.html', {'form': form})

@login_required(login_url='login')
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course added successfully!')
            return redirect('course')
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})

@login_required(login_url='login')
def add_tuition(request):
    if request.method == 'POST':
        form = TuitionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tuition added successfully!')
            return redirect('tuition')
    else:
        form = TuitionForm()
    return render(request, 'add_tuition.html', {'form': form})

@login_required(login_url='login')
def add_instructor(request):
    if request.method == 'POST':
        form = InstructorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Instructor added successfully!')
            return redirect('instructor')
    else:
        form = InstructorForm()
    return render(request, 'add_instructor.html', {'form': form})

@login_required(login_url='login')
def add_semester(request):
    if request.method == 'POST':
        form = SemesterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Semester added successfully!')
            return redirect('semester')
    else:
        form = SemesterForm()
    return render(request, 'add_semester.html', {'form': form})

@login_required(login_url='login')
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student.html', {'students': students})