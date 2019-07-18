from django.db import models

# Create your models here.
class LostItems(models.Model):
    num = models.AutoField(primary_key=True)
    itemName = models.CharField(db_column='itemName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lostPlace = models.CharField(db_column='lostPlace', max_length=100, blank=True, null=True)  # Field name made lowercase.

