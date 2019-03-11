from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(max_length=64)
    age = models.CharField(max_length=64)
    sex = models.CharField(max_length=64)

    def __str__(self):
        return self.username


class Authors(models.Model):
    name = models.CharField(max_length=50)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name


class AuthorDetail(models.Model):
    sex = models.CharField(max_length=50, choices=(('0', '男'), ('1', '女')))
    email = models.EmailField()
    birth_date = models.DateField()
    author = models.OneToOneField(Authors, on_delete=models.CASCADE)
    # CASCADE：此值设置，是级联删除。
    # PROTECT：此值设置，是会报完整性错误。
    # SET_NULL：此值设置，会把外键设置为null，前提是允许为null。
    # SET_DEFAULT：此值设置，会把设置为外键的默认值。
    # SET()：此值设置，会调用外面的值，可以是一个函数。


class Publisher(models.Model):
    pub_name = models.CharField(max_length=50, verbose_name='名字')
    address =  models.CharField(max_length=50, verbose_name='地址')
    city = models.CharField(max_length=50, verbose_name='城市')
    province = models.CharField(max_length=50, verbose_name='省')
    country = models.CharField(max_length=50, verbose_name='国家')
    site = models.URLField()

    def __str__(self):
        self.pub_name


class Book(models.Model):
    book_name = models.CharField(max_length=50)
    pub_date = models.DateField()
    author = models.ManyToManyField(Authors)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=10)

    def __str__(self):
        return self.book_name

# #------------------获取两张表中两个字段唯一
# class Book2Author(models.Model):
#     book = models.ForeignKey(Book)
#     author = models.ForeignKey(Authors)
#     description = models.CharField(max_length=10)
#     class Meta:
#         unique_together = ['book', 'author']


#新增记录两种方式,create save
#-------------------create
#Authors.objects.create(name='jiangqijun')
# Authors.objects.create(**{'name':'xiaoming'})
# #-------------------save
# author1 = Authors(name='xiaohua')
# author1.save()
# author2 = Authors()
# author2.name='xiaoli'
# author2.save()
#
# #新增记录存在唯一外键
# #方式1,直接写入外键的字段名字并且加上id
# #方式2,查询出外键的记录，作为一个对象赋值
# AuthorDetail.objects.create(sex='男', email='test01@qq.com', birth_date='2019-03-10', authors_id=1)
# author_detail = AuthorDetail(sex='女', email='test02@qq.com', birth_date='2019-03-11', authors_id=2)
# author_detail.save()
# #-------------------
# author3 = Authors.objects.get(id=3)
# AuthorDetail.objects.create(sex='男', email='test01@qq.com', birth_date='2019-03-10', authors_id=author3)
#
# #publisher新增记录
# Publisher.objects.create(pub_name='才华有限公司1', address='华中地区', city='永州', province='湖南', country='中国',site='www.baidu.com')
# Publisher.objects.create(pub_name='才华有限公司2', address='华南地区', city='深圳', province='广东', country='中国',site='www.baidu.com')
# Publisher.objects.create(pub_name='才华有限公司3', address='华中地区', city='长沙', province='湖南', country='中国',site='www.baidu.com')
#
# #新增记录存在一对多的外键
# #------------------直接添加publisher_id
# Book.objects.create(book_name='python', pub_date='2019-09-05', publisher_id='1', price='99')
# Book.objects.create(book_name='java', pub_date='2019-09-05', publisher_id='1', price='98')
# Book.objects.create(book_name='c#', pub_date='2019-09-05', publisher_id='2', price='98')
# #-------------------添加publiser对象
# publisher_obj = Publisher.objects.get(id=2)
# Book.objects.create(book_name='c#', pub_date='2019-09-05', publisher_id=publisher_obj, price='98')
#
# #新增记录存在多对多的外键
# #1、如果是通过ManyToManyField创建的，会自动创建第三张表，通过下面的方式进行创建
# #-------------------查询到两个对象的记录，再进行关联
# book_obj1 = Book.objects.get(id=1)
# authors_obj1 = Authors.objects.get(id=1)
# authors_obj2 = Authors.objects.filter(name='jiangqijun')[0]
# book_obj1.author.add(authors_obj1,authors_obj2)
#
# #-------------------查询到两个对象的记录，再进行关联
# book_obj2 = Book.objects.filter(price=98)
# authors_obj3 = Authors.object.filter(name='jiangqijun')[0]
# authors_obj3.book_set.add(*book_obj2)

