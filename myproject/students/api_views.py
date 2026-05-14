from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student, Course


# class HelloAPIView(APIView):
#     def get(self,request):
#         data = {
#             "message" : "Hello DRF"
#         }

#         return Response(data)





# class StudentListViewAPI(APIView):
#     def get(self,request):
#         student = Student.objects.all()
#         data = []
#         for s in student: 
#             data.append({
#                 "address":s.address,
#                 "age" : s.age,
#                 "course_id":s.course.id

#             })
#         return Response(data)


from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

class StudentListViewAPI(APIView):

    def get(self, request):

        students = Student.objects.all()

        serializer = StudentSerializer(students, many=True)

        return Response(serializer.data)