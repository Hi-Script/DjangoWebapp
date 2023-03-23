from django.contrib import admin
from .models import Review, Contact, Blogpost, Comment
# Register your models here.

admin.site.register(Review)
admin.site.register(Contact)
admin.site.register(Blogpost)
admin.site.register(Comment)

