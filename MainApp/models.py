from django.db import models
from django.conf  import settings

class Trade(models.Model):
# Create your models here.
 id=models.AutoField(primary_key=True)
 Open=models.DecimalField
 high=models.DecimalField
 low=models.DecimalField
 close=models.DecimalField
 date=models.DateField