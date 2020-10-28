from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout, update_session_auth_hash
from django.http import HttpResponse
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from .models import *
from sign.models import *
from manager.models import *
from customer.models import *

def home(request):
    user = request.user
    username = user.username
    print(username)
    latest_bookstores = Bookstore.objects.all().order_by('reg_date')
    random_bookstores = Bookstore.objects.all().order_by('?')
    print(latest_bookstores)
    print(random_bookstores)
    return render(request, 'home.html',{'username':username, 'latest_bookstores':latest_bookstores, random_bookstores:'random_bookstores'})


def mypage(request):
    user = request.user
    username = user.username
    print(username)
    return render(request, 'mypage.html',{'username':username})
    

def map(request):
    return render(request, 'map.html')

def subscription(request):
    return render(request, 'subscription.html')

def tag_result(request):
    user = request.user
    usertag = UserTag.objects.filter(username=user).all()
    taglist= []
    for tag in usertag:
        taglist.append(tag.tag_id)
    print(taglist)
    tag1 = taglist[0]
    tag2 = taglist[1]
    tag3 = taglist[2]
    
    return render(request, 'tag_result.html', {'tag1':tag1, 'tag2':tag2, 'tag3':tag3} )

def customer_info(request):
    user = request.user
    return render(request, 'customer_info.html', {'user':user})

def my_reply(request):
    return render(request, 'my_reply.html')


def add_complain(request):
    new_complain = Complain()
    new_complain.complain = request.GET['text']
    new_complain.save()
    return render(request, 'home.html')

    
def serach_bookstore(request):
    bookstore_name = request.GET['bookstore_name']
    bookstore = Bookstore.objects.get(name=bookstore_name)
    print(bookstore.name)
    return render(request, 'result_store.html' , {'bookstore':bookstore})
# Create your views here.
