from django.db import models

class TestingDatabase(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name}"

class Course(models.Model):
    course_name = models.CharField()
    instructor_name = models.CharField()
    start_date = models.DateField()
    end_date = models.DateField()
    course_id = models.IntegerField()

    def __str__(self):
        return f"{self.course_name}"

class Tuition(models.Model):
    payment_id = models.IntegerField()
    student_id = models.IntegerField()
    amount = models.IntegerField()
    payment_date = models.DateField()
    payment_status = models.CharField(
        choices=[('Paid','Paid'), ('Unpaid', 'Unpaid')],
        default='Paid'
    )

    def __str__(self):
        return f"{self.student_id}"

class Instructor(models.Model):
    instructor_id = models.CharField()
    name = models.CharField()
    email = models.EmailField()
    contact_number = models.IntegerField()
    courses_taught = models.CharField()

    def __str__(self):
        return f"{self.name}"

class Semester(models.Model):
    semester_id = models.CharField()
    semester_name = models.CharField()
    start_date = models.DateField()
    end_date = models.DateField()
    status_status = models.CharField(
        choices=[('Enrolled','Enrolled'), ('Unenrolled', 'Unenrolled')],
        default='Enrolled'
    )

    def __str__(self):
        return f"{self.semester_id}"

class Student(models.Model):
    name = models.CharField()
    password = models.CharField()
    email = models.EmailField()
    birthdate = models.DateField()
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name}"