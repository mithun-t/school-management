from django.http import HttpResponse
from django.shortcuts import redirect, render
from Home.models import Department,Student,Teacher
from Home.forms import Dep_form,UserForm, StudentForm,TeacherForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login


# Create your views here.
def add_department(request):
     if request.method == 'POST':
        form = Dep_form(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponse("success")
            return HttpResponse("<script>window.alert('successfully added');window.location.href='/dep_view/'</script>")
     else:
        form = Dep_form()
        return render(request, 'add_department.html', {'form': form})

def dep_view(request):
    depnames=Department.objects.all()
    return render(request,'department_view.html',{'depnames':depnames})

def dep_del(request, dep_id):
    dep_name=Department.objects.get(id=dep_id)
    dep_name.delete()
    return HttpResponse("<script>window.alert('successfully deleteed');window.location.href='/dep_view/'</script>")



def add_student(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        student_form = StudentForm(request.POST)
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.is_active=False
            user.save()
            student = student_form.save(commit=False)
            student.user = user
            student.save()
            return HttpResponse("<script>window.alert('successfully added');window.location.href='/view_students/'</script>")
            # return redirect('view_students')
    else:

        user_form = UserForm()
        student_form = StudentForm()
    return render(request, 'add_student.html', {'user_form': user_form, 'student_form': student_form})

def view_students(request):
    students = Student.objects.all()
    return render(request, 'view_students.html', {'students': students})

def approve(request,student_id):
    approve_stud=Student.objects.get(id=student_id)
    user = approve_stud.user
    user.is_active=True
    user.save()
    return redirect('view_students')

def disapprove(request,student_id):
    disapprove_stud=Student.objects.get(id=student_id)
    user = disapprove_stud.user
    user.is_active=False
    user.save()
    return redirect('view_students')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('home')  
            else:
                return HttpResponse("<script>window.alert('Invalig login details');window.location.href='/login/'</script>")
        else:
            return HttpResponse("<script>window.alert('Invalig login details');window.location.href='/login/'</script>")
    return render(request, 'login.html')



def home(request):
    user = request.user
    if hasattr(user, 'student'):
        department = user.student.department
    elif hasattr(user, 'teacher'):
        department = user.teacher.department
    else:
        department = None
    return render(request, 'home.html', {'user': user, 'department': department})

def edit_student(request):
    user = request.user
    student = Student.objects.get(user=user)
    
    if request.method == 'POST':
        
        student_form = StudentForm(request.POST, instance=student)
        if student_form.is_valid():
            student_form.save()
            return redirect('home')  
    else:
        
        student_form = StudentForm(instance=student)
    
    return render(request, 'edit_student.html', {
        
        'student_form': student_form
    })


def add_teacher(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        teacher_form = TeacherForm(request.POST)
        if user_form.is_valid() and teacher_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.is_staff=True
            user.save()
            teacher = teacher_form.save(commit=False)
            teacher.user = user
            teacher.save()
            return HttpResponse("<script>window.alert('successfully saved');window.location.href='/teacher_view/'</script>")

    else:

        user_form = UserForm()
        teacher_form = TeacherForm()
    return render(request, 'add_teacher.html', {'user_form': user_form, 'teacher_form': teacher_form})

def teacher_view(request):
    teachers = Teacher.objects.all()
    return render(request, 'view_teacher.html', {'teachers': teachers})

def teacher_del(request,teacher_id):
    teacher=Teacher.objects.get(id=teacher_id)
    teacher.delete()
    return HttpResponse("<script>window.alert('successfully deleted');window.location.href='/teacher_view/'</script>")

    
    
def edit_teacher(request):
    user = request.user
    teacher = Teacher.objects.get(user=user)
    
    if request.method == 'POST':
        teacher_form = TeacherForm(request.POST, instance=teacher)
        if teacher_form.is_valid():
            teacher_form.save()
            return redirect('home')  
    else:
        
        teacher_form = TeacherForm(instance=teacher)
    
    return render(request, 'edit_teacher.html', {
        'teacher_form': teacher_form
    })

 


def view_students_by_dep(request, department_id):
    if department_id:
        department = Department.objects.get(id=department_id)
        students = Student.objects.filter(department=department)
    return render(request, 'view_students.html', {'students': students, 'department_id': department_id})

def view_teachers_by_dep(request, department_id):
    if department_id:
        department = Department.objects.get(id=department_id)
        teachers = Teacher.objects.filter(department=department)
    return render(request, 'view_teacher.html', {'teachers': teachers, 'department_id': department_id})


from django.http import FileResponse
from reportlab.pdfgen import canvas
from io import BytesIO

def generate_pdf(request):
    # Create a file-like buffer to receive PDF data
    buffer = BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

