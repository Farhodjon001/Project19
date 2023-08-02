from django.shortcuts import render
from .models import Pupil
from django.http import JsonResponse
# Create your views here.

def get_all(request):
    if request.method=="GET":
        all_date= Pupil.objects.all()
        result=[]
        for pupil in all_date:
             result.append({"id":pupil.id,"pupil_name":pupil.first_name})
        return JsonResponse({"date":result})

def get_by_id(request,pupil_id):
    if request.method=="GET":
        try:
            date=Pupil.objects.get(id=pupil_id)
        except Pupil.DoesNotExists:
            return JsonResponse({"msg": "NOT FOUND"})
        return JsonResponse({"id":date.id,"pupil_name":date.first_name})