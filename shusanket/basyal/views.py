from functools import partial
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
# @api_view()
# def hello(request):
#     return Response("HELLO WORLD")
# ============================== GET REQUEST WITHOUT USING GET.


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def hello(request, pk=None):
    if request.method=="GET":
        id  = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            stuserializer = StudentSerializer(stu)
            return Response(stuserializer.data,status=status.HTTP_200_OK)
        
        stu= Student.objects.all()
        stuserializer = StudentSerializer(stu, many=True)
        return Response(stuserializer.data, status=status.HTTP_200_OK)
        


    if request.method == "POST":
        serializer = StudentSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"YOUR DATA HAS BEEN SAVED!!"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"YOUR DATA HAS BEEN UPDATED"}, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
    if request.method=="DELETE":
        id = pk
        stu = Student.objects.get(pk=id) 
        stu.delete()
        return Response({"msg":"DELETEDDDDDDDDDDDDDDDD"}, status=status.HTTP_202_ACCEPTED)   
