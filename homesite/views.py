from django.shortcuts import render, redirect
from .models import Review, Contact, Blogpost, Comment
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden, HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from hiscript.decorators import superuser_required
from django.core.mail.message import EmailMessage
from django.core import mail
from django.contrib import messages
# Create your views here.

def index(request):
    context={}
    reviews = Review.objects.all()
    blogpost = Blogpost.objects.all()
    context = {'reviews': reviews, 'blogpost': blogpost}
    return render(request, 'index.html', context )

@superuser_required(message='You are not authorized', login_url='login', redirect_field_name='')
def Blogs(request):

    context={}
    if request.method == 'POST':
       
        
        try:
            Blogpost.objects.create(
                title= request.POST.get('f-title'),
                category= request.POST.get('categories'),
                description = request.POST.get('fe-description'),
                body= request.POST.get('f-description'),
                blog_pic = request.FILES.get('f-image'),
                author= request.user
                
            )
            return redirect('home')
        except:
            context ['message'] = "invalid details"

    return render(request, 'blogcreate.html', context)    


def getblogPost(request, pk):
    blog = Blogpost.objects.get(id=pk)

    if request.method == 'POST':
        comment = request.POST.get('comment')
        Comment.objects.create(
            blog=blog,
            author = request.user,
            comment = comment
        )


    
        
    
    return render(request, 'blogpost.html', {'blog': blog})


def ContactPage(request):
    context= {}
    if request.method == 'POST':
       
        
        
        
        fname= request.POST.get('fullname')
        femail = request.POST.get('email')
        descr= request.POST.get('message')
        query= Contact(name=fname, email=femail, message=descr)
        query.save()
        #sendmail
        from_email= settings.EMAIL_HOST_USER
        connection=mail.get_connection()
        connection.open()
        email_message=mail.EmailMessage( f'Email from {fname}', f'UserEmail: {femail}\n\n\n QUERY : {descr}', from_email,
                                        ['officialhiscript@gmail.com', 'tundeadeoye9@gmail.com'],
                                         connection= connection)

        email_client=mail.EmailMessage( 'HiScript Response', 'Thanks For Reaching out to us, we will get back to you shortly\n\nHiScript Teams\n+2348105008555', from_email,
                                        [femail],
                                         connection= connection)                                  
        connection.send_messages([email_message,email_client,])
        connection.close()
        messages.INFO=(request, f'{fname}, Thanks For Reaching Us! We will get to you shortly.')
        return redirect('success')
        
        context = {'fname': fname}
        


    return render(request, 'contact.html', context)

def Aboutpage(request):
    context = {}
    return render(request, 'about.html', context)

def Response(request):
    context = {}
    return render(request, 'response.html', context)

def Reviewpage(request):

    context={}
    if request.method == 'POST':
       
        
        try:
            Review.objects.create(
                name= request.POST.get('name'),
                job= request.POST.get('Job'),
                reviewer_pic = request.FILES.get('image'),
                body= request.POST.get('description'),
                
            )
            return redirect('home')
        except:
            context ['message'] = "invalid details"

    return render(request, 'review.html', context)    


