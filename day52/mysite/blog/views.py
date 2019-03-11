from django.shortcuts import render, HttpResponse, redirect
from blog import models
import datetime
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


def show(req):
    #新增记录两种方式,create save
    # #-------------------create
    # models.Authors.objects.create(name='jiangqijun')
    # models.Authors.objects.create(**{'name':'xiaoming'})
    # #-------------------save
    # author1 = models.Authors(name='xiaohua')
    # author1.save()
    # author2 = models.Authors()
    # author2.name='xiaoli'
    # author2.save()
    #
    # #新增记录存在唯一外键
    # #方式1,直接写入外键的字段名字并且加上id
    # #方式2,查询出外键的记录，作为一个对象赋值
    # models.AuthorDetail.objects.create(sex='男', email='test01@qq.com', birth_date='2019-03-10', author_id=1)
    # author_detail = models.AuthorDetail(sex='女', email='test02@qq.com', birth_date='2019-03-11', author_id=2)
    # author_detail.save()
    #-------------------
    # author3 = models.Authors.objects.get(id=3)
    # models.AuthorDetail.objects.create(sex='男', email='test01@qq.com', birth_date='2019-03-10', author=author3)

    # #publisher新增记录
    # models.Publisher.objects.create(pub_name='才华有限公司1', address='华中地区', city='永州', province='湖南', country='中国',site='www.baidu.com')
    # models.Publisher.objects.create(pub_name='才华有限公司2', address='华南地区', city='深圳', province='广东', country='中国',site='www.baidu.com')
    # models.Publisher.objects.create(pub_name='才华有限公司3', address='华中地区', city='长沙', province='湖南', country='中国',site='www.baidu.com')

    #新增记录存在一对多的外键
    # #------------------直接添加publisher_id
    # models.Book.objects.create(book_name='python', pub_date='2019-09-05', publisher_id='1', price='99')
    # models.Book.objects.create(book_name='java', pub_date='2019-09-05', publisher_id='1', price='98')
    # models.Book.objects.create(book_name='c#', pub_date='2019-09-05', publisher_id='2', price='98')
    # #-------------------添加publiser对象
    # publisher_obj = models.Publisher.objects.get(id=3)
    # models.Book.objects.create(book_name='c#', pub_date='2019-09-05', publisher=publisher_obj, price='98')

    # #新增记录存在多对多的外键
    # #1、如果是通过ManyToManyField创建的，会自动创建第三张表，通过下面的方式进行创建
    # #-------------------查询到两个对象的记录，再进行关联
    # book_obj1 = models.Book.objects.get(id=1)
    # authors_obj1 = models.Authors.objects.get(id=1)
    # authors_obj2 = models.Authors.objects.filter(name='jiangqijun')[1]
    # book_obj1.author.add(authors_obj1,authors_obj2)

    #-------------------查询到两个对象的记录，再进行关联
    # book_obj2 = models.Book.objects.filter(price=98)
    # authors_obj3 = models.Authors.objects.filter(name='jiangqijun')[0]
    # authors_obj3.book_set.add(*book_obj2)

    # -------------------查询api，总共三种方式
    #author_detail_obj=models.AuthorDetail.objects.all()#返回所有的记录
    # print(type(author_detail_obj))
    # for obj in author_detail_obj:
    #     print(obj.sex)
    # print(author_detail_obj[0])

    # print(models.AuthorDetail.objects.filter(sex='男')) #返回多个结果
    # print(models.AuthorDetail.objects.get(sex='女')) #返回结果只能又一个，超过的话就会报错
    # print(models.AuthorDetail.objects.all().values('email'))
    print(models.AuthorDetail.objects.all().values_list('email','id'))

    #---删除普通删除
    #models.AuthorDetail.objects.filter(id=4).delete()

    return render(req, "show.html")