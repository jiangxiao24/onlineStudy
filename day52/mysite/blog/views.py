from django.shortcuts import render,HttpResponse,redirect
from blog import models
import  datetime
#from models import  Userinfo

# Create your views here.s
info_list = []


def testweb(req):
    if req.method == "POST":
        u = req.POST.get("username", None)
        s = req.POST.get("sex",None)
        a = req.POST.get("age", None)
        userinfo = {"username": u, "sex": s, "age": a}
        models.UserInfo.objects.create(
            username = u,
            age = a,
            sex = s
        )
        info_list = models.UserInfo.objects.all()
        return render(req, "testweb.html", {"info_list":info_list})
    return render(req, "testweb.html")


def year_arcives(req):
    return HttpResponse("2018")


def year_month_param(req, year, month):
    return  HttpResponse("year"+year+"month"+month)


def year_month_noorder(req, month, year):
    return HttpResponse("year"+year+"month"+month)


template_list = []
def template_para(req):
    if req.method == "POST":
        u = req.POST.get('username')
        s = req.POST.get('password')
        if u == 'jiangqijun'and s == 'jiangqijun':
            print(req.path)
            return HttpResponse("登陆成功1")
    return render(req, "login.html")
    #return HttpResponse(req, "login.html")


def test(req):
    return HttpResponse("这是一个默认页面")


def req_property(req):
    if req.method == "POST":
        aa = "aaa"
        bb = "bbb"
        cc = "ccc"
        print(req.POST)
        if 1:
            return  render(req, 'req_property.html', locals()) #如果前端action传了调用页面则这里失效
    print(req.path)
    return render(req, 'req_property.html')
    #return  redirect('http://www.baidu.com')进行重定向

def loggin(req):
    if req.method == 'POST':
        #return render(req, 'home.html')
       return redirect('/home/')  # 这里一定要用两个/否则无法解释出来
    #return redirect('home/')
    else:
        return render(req, 'loggin.html')

def home(req):
    name = 'jiangqijun'
    return  render(req, 'home.html', locals())

def current_time(req):
    abc = datetime.datetime.now()
    return render(req, 'currenttime.html', {'abc':abc})

def template_content(req):
    s1 = ['aa', 'bb', 'cc']
    s2 = {'name': 'jiangqijun', 'sex': 'female'}
    s3 = 10
    s4 = '<a href = "#">跳转</a>'
    name = 'efg'
    return render(req, 'index.html', locals())