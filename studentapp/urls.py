from django.urls import path

from studentapp import views

urlpatterns=[
    path('',views.mainpage,name='mainpage'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('adminpage',views.adminpage,name='adminpage'),
    path('student',views.student,name='student'),
    path('register',views.register,name='register'),
    path('student_view',views.student_view,name='student_view'),
    path('delete_student/<int:id>/',views.delete_student,name='delete_student'),
    path('mark',views.mark,name='mark'),
    path('student_profile',views.student_profile,name='student_profile'),
    path('update_student/<int:id>/',views.update_student,name='update_student'),
    path('logout_view',views.logout_view,name='logout_view'),
    path('mark_view',views.mark_view,name='mark_view'),
    path('mview',views.mview,name='mview'),


]


