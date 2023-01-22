from ctypes import resize
from distutils.command.upload import upload
import email
from email.policy import default
from pickle import TRUE
from statistics import mode
from turtle import title, update
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
 
class Review(models.Model):
    name = models.CharField(max_length=100, null=TRUE)
    job = models.CharField(max_length=100, null=TRUE)
    reviewer_pic = models.ImageField(null=TRUE, blank=TRUE, upload_to='images/')
    body = models.TextField(null=TRUE)
    created= models.DateTimeField(auto_now_add=TRUE,null=TRUE)



    class Meta:
        ordering =['-created']


    def __str__(self):
        return self.name  
