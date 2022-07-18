from datetime import datetime
from sqlite3 import Date
from django.db import models

class Comment(models.Model):
    new_date = datetime.now()
    name = models.CharField(max_length=255, null=False)
    score = models.IntegerField(default=3)
    comment = models.TextField(max_length=1000, null=True)
    date = models.DateField(null=True, default=new_date)
    signature = models.CharField(max_length=100, default="firma")

    def __str__(self):
        return self.name

