#__author__:jiangqijun
#__date__:2019/1/24

from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'testweb/', views.testweb),
    url(r'^articles/2018/$', views.year_arcives),
    #url(r'^articles/([0-9]{4})/([0-9]{2})$', views.year_month_param), #可以获取参数的值
    url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})$', views.year_month_noorder), # 这里传入的两个变量year,month可以调换位置
    #url(r'articles/index', views.template_para, {'name':'jiangqijun'}), # 这里是把这个参数传给views中
    url(r'articles/index', views.template_para), # 这里是把这个参数传给views中
    url(r'test/', views.test, name= 'bieming'),
    url(r'req_property/',views.req_property),
    url(r'current/',views.current_time),
    url(r'index/', views.template_content),
    url(r'show',views.show),
    url(r'authordetail',views.AuthorsDetail.as_view())
]