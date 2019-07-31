from django.db import models

# Create your models here.
class LostItems(models.Model):
    num = models.AutoField(primary_key=True) #데이터 번호(primary key)
    managementID = models.CharField(db_column='managementID', max_length=100, blank=True, null=True) #관리ID
    findYmd = models.CharField(db_column='findYmd', max_length=100, blank=True, null=True) #습득일자
    productName = models.CharField(db_column='productName', max_length=100, blank=True, null=True) #물품명
    keepPlace = models.CharField(db_column='keepPlace', max_length=100, blank=True, null=True) #보관장소
    productImg = models.CharField(db_column='productImg', max_length=100, blank=True, null=True) #이미지
    productDesc = models.CharField(db_column='productDesc', max_length=200, blank=True, null=True) #물품상세설명
    productClass = models.CharField(db_column='productClass', max_length=100, blank=True, null=True) #물품분류명

class LostItemsTemp(models.Model):
    num = models.AutoField(primary_key=True) #데이터 번호(primary key)
    managementID = models.CharField(db_column='managementID', max_length=100, blank=True, null=True) #관리ID
    findYmd = models.CharField(db_column='findYmd', max_length=100, blank=True, null=True) #습득일자
    productName = models.CharField(db_column='productName', max_length=100, blank=True, null=True) #물품명
    keepPlace = models.CharField(db_column='keepPlace', max_length=100, blank=True, null=True) #보관장소
    productImg = models.CharField(db_column='productImg', max_length=100, blank=True, null=True) #이미지
    productDesc = models.CharField(db_column='productDesc', max_length=200, blank=True, null=True) #물품상세설명
    productClass = models.CharField(db_column='productClass', max_length=100, blank=True, null=True) #물품분류명





