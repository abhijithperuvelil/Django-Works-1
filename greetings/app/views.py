from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

# Create your views here.
class GoodMorning(View):
    def get(self,request):
        data={"message":"Good Morning"}
        return JsonResponse(data)
class GoodAfternoon(View):
    def get(self,request):
        data={"message":"Good Afternoon"}
        return JsonResponse(data)
class GoodEvening(View):
    def get(self,request):
        data={"message":"Good Evening"}
        return JsonResponse(data)
class GoodNight(View):
    def get(self,request):
        data={"message":"Good Night"}
        return JsonResponse(data)

class Userdetails(View):
    def get(self,request):
        data=[ {'name':'arun','age':23,'place':'ekm'},
            {'name':'amal','age':23,'place':'ktm'},
            {'name':'anu','age':23,'place':'tcr'}]
        return JsonResponse(data,safe=False)


