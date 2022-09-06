from unicodedata import category
from django.db import models

# Create your models here.


class CategoryPost(models.Model):
     nombre:models.CharField(max_length=100)
     estado = models.BooleanField('estado',null=True,default=True)

class Post(models.Model):

     nombre = models.CharField(unique=True,max_length=100)
     estado = models.BooleanField('estado',null=True,default=True)
     category = models.ForeignKey(CategoryPost,on_delete=models.PROTECT)