from django.shortcuts import render, redirect

from myApp.models import SlideShow, MainDescription, Product, CategorieGroup, ChildGroup, User, Address, Cart, Order
import random
# from dysms_python.demo_sms_send import send_sms
from django.http import JsonResponse
import uuid
from myApp.serializers import SlideShowSerializer,MainDescriptionSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


# Create your views here.
@csrf_exempt
def home(request):
    if request.method == 'GET':
        lbt = SlideShow.objects.all()
        serializer = SlideShowSerializer(lbt,many=True)
        return JsonResponse(serializer.data,safe=False)
def market(request, gid, cid, sid):
    pass
def detail(request):
    pass
def mine(request):
    pass
def quit(request):
    pass
def login(request):
    pass
def map(request):
    pass
def showAddress(request):
   pass
def addAddress(request):
    pass
def cart(request):
    pass
def changecart(request, flag):
    pass
def changecart2(request):
    pass
def search(request):
    pass
def myweb(request):
    pass
def qOrder(request):
    pass


