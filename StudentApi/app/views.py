from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from django.views import View
class Student(View):
    def get(self,request):
        data={'Name':'Arun','Age':23,'Course':'Python','Marks':45,
        }
        return JsonResponse(data)
class StudentList(View):
    def get(self,request):
        data=[{'Name':'Arun','Age':23,'Course':'Python','Marks':45,
        },
        {'Name':'Amal','Age':24,'Course':'Java','Marks':46,
        },
        {'Name': 'Anu', 'Age': 23, 'Course': 'Testing', 'Marks': 47,
         }]
        return JsonResponse(data,safe=False)

