#__author__:jiangqijun
#__date__:2019/4/23

from rest_framework import serializers
from blog import models


class AuthorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Authors
        feilds = ('id', 'name')

class AuthorDetailSerializers(serializers.ModelSerializer):
    authors_name = serializers.CharField(source='author.name')
    authors_id = serializers.CharField(source='author.id')
    class Meta:
        model = models.AuthorDetail
        fields = '__all__'