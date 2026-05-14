# from django.urls import path 
# from . import views
# urlpatterns = 
#     path('',views.home), 
#     path('about/',views.about),
#     path('students/',views.students)
# ]


# from django.urls import path
# from .views import home, student_list,create_student,student_detail,update_student,delete_student,StudentListView

# urlpatterns = [
#     path('', home),
#     path('students/', student_list),

#     path('students/<int:id>/', student_detail), #so this means when a ceratain student/any int/ is found it takes to student_details
#    path('create/<int:age>/<str:address>/<int:course_id>/', create_student),
#    path('update/<int:id>/<str:new_address>/',update_student),
#    path('delete/<int:id>/',delete_student),
#    path('students/', StudentListView.as_view())
   
# ]


from django.urls import path
from .views import UpdateStudent

urlpatterns = [
    path('search/<int:id>/',UpdateStudent.as_view()),
    
]