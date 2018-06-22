from django.db import models

# Create your models here.

class SlideShow(models.Model):
    trackid = models.CharField(max_length=20)
    name    = models.CharField(max_length=20)
    img     = models.CharField(max_length=150)
    sort    = models.CharField(max_length=20)
    class Meta:
        db_table = "slideshows"
        ordering = ['sort']


'''
id(商品id的值)
name            商品名
long_name       商品名+规格
productId      商品id
storeNums      库存
salesVolume    销量
specifics       规格
sort            排序   
marketPrice    超市价格  
price           价格     
categoryId     分组id
childId       子组id
img             商品图片
keywords        搜索关键字
brandId        品牌id
brandName      品牌名称
safeDay        保质期长度
safeUnit       保质期单位模式
safeUnitDesc   保质期单位 
'''

class Product(models.Model):
    name = models.CharField(max_length=100)
    longName = models.CharField(max_length=150)
    productId = models.CharField(max_length=20)
    storeNums = models.CharField(max_length=20)
    # salesVolume = models.CharField(max_length=20)
    specifics = models.CharField(max_length=20)
    sort = models.CharField(max_length=20)
    marketPrice = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    categoryId = models.CharField(max_length=20)
    childId = models.CharField(max_length=20)
    img = models.CharField(max_length=200)
    keywords = models.CharField(max_length=100)
    brandId = models.CharField(max_length=20)
    brandName = models.CharField(max_length=100)
    safeDay = models.CharField(max_length=20)
    safeUnit = models.CharField(max_length=20)
    safeUnitDesc = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    dfsf = models.C