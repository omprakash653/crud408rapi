# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Student
# from .serializers import StudentSerializer
# from rest_framework import status

# # Create your views here.
# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def student_api(request):
#     if request.method == 'GET':
#         id = request.data.get('id')
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)

#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors)

#     if request.method == 'PUT':
#         id = request.data.get('id')
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Updated'})
#         return Response(serializer.errors)

#     if request.method == 'DELETE':
#         id = request.data.get('id')
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg':'Data Deleted'})


from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

@api_view(['GET'])
def get_student(request, id=None):
    return Response(StudentSerializer(get_object_or_404(Student, id=id) if id else Student.objects.all(), many=not id).data)

@api_view(['POST'])
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    return Response({'msg': 'Student Created'} if serializer.is_valid() and serializer.save() else serializer.errors)

@api_view(['PUT'])
def update_student(request, id):
    serializer = StudentSerializer(get_object_or_404(Student, id=id), data=request.data, partial=True)
    return Response({'msg': 'Student Updated'} if serializer.is_valid() and serializer.save() else serializer.errors)

@api_view(['DELETE'])
def delete_student(request, id):
    get_object_or_404(Student, id=id).delete()
    return Response({'msg': 'Student Deleted'})
