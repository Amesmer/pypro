from django.shortcuts import render, HttpResponse, redirect
from django.middleware.csrf import get_token
from django.http import JsonResponse

# Create your views here.


def index(request):
    # request是一个对象 封装了用户发过来的所有请求相关数据
    # 1 获取请求方式  get/post
    print(request.method)
    # 2 在url传递参数
    print(request.GET)
    # 3 在请求体中提交数据
    print(request.POST)
    # 4 HttpResponse返回字符串内容
    return HttpResponse('')
    # 5返回页面渲染
    # return render(request, 'user_list.html',{"title":"来了"})
    # 6重定向
    # return redirect("https://www.baidu.com/")
# render 方法执行渲染


def user_list(request):
    return render(request, 'user_list.html')


def user_add(request):
    return HttpResponse('useradd success')


def login(request):
    print(request.POST)
    # username=request.POST.get('username')
    # password=request.POST.get('password')
    # print(username,password)
    return JsonResponse({'csrf_token': get_token(request) or 'NOTPROVIDED'})
