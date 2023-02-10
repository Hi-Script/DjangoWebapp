
from pickle import TRUE
from django.db import models



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
