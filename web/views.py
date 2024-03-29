from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from web.models import Expense ,Income , token
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
# Create your views here.
# TODO:  amount validate date ,user might be fake ,token might be fake
@csrf_exempt
def submit_expense(request):
    print (request.POST)
    now =datetime.now()
    this_token=request.POST.get('token')
    this_user=User.objects.get()
    Expense.objects.Create(user=this_user,text=request.POST.get('text'),
    amount=request.POST.get("amount"),date=now)
    return JsonResponse({
    "status":"ok"
    },encoder=JSONEncoder)
