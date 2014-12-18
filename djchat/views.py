from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
import simplejson


def chat_login(request):
    username = request.POST['username']
    # username = 'admin'
    password = request.POST['password']
    # password = 'mzh50537381'
    print username
    print password
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            result = "login_success"
            result = simplejson.dumps(result)
        else:
            result = "login_invalid"
            result = simplejson.dumps(result)
    else:
        result = "login_failed"
        result = simplejson.dumps(result)
    return HttpResponse(result, content_type='application/javascript')

def chat_register(request):
    # print "test"
    username = request.POST['username']
    password = request.POST['password']
    try:
        user = User.objects.get(username=username)
        result = "user_exist"
        result = simplejson.dumps(result)
        return HttpResponse(result, content_type='application/javascript')
    except Exception  as e:
        print e.message;
        print request.POST['username']
        print request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return chat_login(request)


def chat_logout(request):
    logout(request)
    return redirect("../rooms/")


