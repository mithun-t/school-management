"""
URL configuration for school project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path
from Home import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_dep/',views.add_department),
    path('dep_view/',views.dep_view),
    path('dep_del/<int:dep_id>/',views.dep_del,name='dep_view'),
    path('add_student/',views.add_student),
    path('view_students/',views.view_students,name='view_students'),
    path('approve/<int:student_id>/',views.approve),
    path('disapprove/<int:student_id>/',views.disapprove),
    path('',views.login),
    path('home/', views.home, name='home'),
    path('edit_student/',views.edit_student),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('add_teacher/',views.add_teacher),
    path('teacher_view/',views.teacher_view,name='teacher_view'),
    path('teacher_del/<int:teacher_id>/',views.teacher_del,name='teacher_view'),
    path('edit_teacher/',views.edit_teacher),
    path('view_students_by_dep/<int:department_id>/',views.view_students_by_dep,name='view_students_by_dep'),
    path('view_teachers_by_dep/<int:department_id>/',views.view_teachers_by_dep,name='view_teachers_by_dep'),



]
