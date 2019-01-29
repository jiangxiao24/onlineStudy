#__author__:jiangqijun
#__date__:2019/1/28

from django import template

register = template.Library()

@register.simple_tag
def my_add(v1):
    return  v1+100

