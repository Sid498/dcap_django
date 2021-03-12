from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
import json


@api_view(['GET'])
def list_emp(request):
    all_emp = Employee.objects.all()
    data = EmployeeSerializer(all_emp, many=True)
    return JsonResponse({'emp': data.data}, status=status.HTTP_200_OK)

@api_view(['POST', 'GET'])
@csrf_exempt
def add_emp(request):
    serializer = EmployeeSerializer(data=request.data)

    if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE', 'GET'])
def delete_emp(request, id):
    # http://localhost:8000/remove/6
    try:
        emp = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return JsonResponse({'Error': 'Employee does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = Employee(emp)
        return JsonResponse(serializer.data)
    elif request.method == "DELETE":
        emp.delete()
        return JsonResponse({'message': 'Employee was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def update_emp(request, id):
    # http://localhost:8000/update/5

    try:
        emp = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return JsonResponse({'Error': 'Employee does not exist'}, status=status.HTTP_404_NOT_FOUND)

    emp_serializer = EmployeeSerializer(emp, data=request.data)
    if emp_serializer.is_valid():
        emp_serializer.save()
        return JsonResponse(emp_serializer.data)
    else:
        return JsonResponse(emp_serializer.errors, status=status.HTTP_400_BAD_REQUEST)