
from pickle import TRUE
from django.db import models
#from imagekit.models import ImageSpecField
#from pilkit.processors import ResizeToFill
from django.contrib.auth.models import User


# Create your models here.
 

#contact model

class Contact(models.Model):
    name = models.CharField(max_length=100, null=TRUE)
    email = models.EmailField(max_length=100, null=TRUE)
    message = models.TextField(null=TRUE)
    created= models.DateTimeField(auto_now_add=TRUE,null=TRUE)

 

    class Meta:
        ordering =['-created']


    def __str__(self):
        return self.name  


class Review(models.Model):
    name = models.CharField(max_length=100, null=TRUE)
    job = models.CharField(max_length=100, null=TRUE)
    reviewer_pic = models.ImageField(null=TRUE, blank=TRUE, upload_to='images/')
    #reviewer_pic_thumbnail = ImageSpecField(source='reviewer_pic',processors=[ResizeToFill(120, 116)],format='JPEG',options={'quality': 60})
    body = models.TextField(null=TRUE)
    created= models.DateTimeField(auto_now_add=TRUE,null=TRUE)



    class Meta:
        ordering =['-created']


    def __str__(self):
        return self.name  

class Blogpost(models.Model):
    title = models.CharField(max_length= 150, null=True, blank=TRUE)
    category = models.CharField( max_length= 150, null=TRUE, blank=TRUE)
    description = models.TextField(null=TRUE, blank=TRUE)
    body = models.TextField(null=TRUE, blank=TRUE)
    blog_pic = models.ImageField(null=TRUE, blank=TRUE, upload_to='feature/')
    #blog_pic_thumbnail = ImageSpecField(source='blog_pic',processors=[ResizeToFill(300, 200)],format='JPEG',options={'quality': 80})
    author= models.ForeignKey(User, on_delete=models.CASCADE, null=TRUE)
    created= models.DateTimeField(auto_now_add=TRUE,null=TRUE)
    updated= models.DateTimeField(auto_now=TRUE, null=TRUE)

    class Meta:
        ordering =['-created']

    def __str__(self):
        return self.title  


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    post = models.ForeignKey('Blogpost', on_delete = models.CASCADE)
    comment = models.CharField(max_length = 100)
    created = models.DateTimeField(auto_now_add=TRUE)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.comment
