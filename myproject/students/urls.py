# from django.urls import path 
# from . import views
# urlpatterns = [
#     path('',views.home), 
#     path('about/',views.about),
#     path('students/',views.students)
# ]


from django.urls import path
from .views import home, student_list, student_detail

urlpatterns = [
    path('', home),
    path('students/', student_list),

    path('students/<int:id>/', student_detail), #so this means when a ceratain student/any int/ is found it takes to student_details 
]