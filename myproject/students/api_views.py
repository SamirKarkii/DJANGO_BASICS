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


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import Student
# from .serializers import StudentSerializer

# class StudentListViewAPI(APIView):

#     def get(self, request):

#         students = Student.objects.all()

#         serializer = StudentSerializer(students, many=True)

#         return Response(serializer.data)

# from rest_framework.views import APIView
# from .models import Student,Course
# from .serializers import StudentSerializer
# from rest_framework.response import Response

# class StudentCreateAPIView(APIView):
#     def post(self,request):
#         serializer = StudentSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 "message" : "Student Created"
#             })
#         return Response(serializer.errors)


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import Student,Course
# from .serializers import StudentSerializer

# class StudentCreateAPIView(APIView):
#     def post(self,request):
#         serializer = StudentSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 "message" : "Student Created"
#             })
#         return Response(serializer.errors)


# from rest_framework.views import View
# from .models import Student
# from .serializers import StudentSerializer
# from rest_framework.response import Response

# class StudentUpdateAPIView(APIView):
#     def patch(self,request,id): 
#         try:
#             student = Student.objects.get(id=id)

#         except Student.DoesNotExist:
#             return Response({
#                 "error" : "Student not found"
#             })
#         serializer = StudentSerializer(
#             instance = student,
#             data = request.data ,
#             partial = True
#         )
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 "message": "Student Updated"
#             })
#         return Response(serializer.errors)

from rest_framework.views import APIView
from .models import Student,Course
from .serializers import StudentSerializer
from rest_framework.response import Response

class StudentDeleteAPIViwe(APIView):
    def delete(self, request, id):

        try:
            student = Student.objects.get(id=id)

        except Student.DoesNotExist:
            return Response({
                "error": "Student not found"
            })

        student.delete()

        return Response({
            "message": "Student deleted successfully"
        })