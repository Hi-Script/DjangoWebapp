from django.shortcuts import render, redirect
from .models import Review


# Create your views here.

def index(request):
    context={}
    reviews = Review.objects.all()
    context = {'reviews': reviews}
    return render(request, 'index.html', context )


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
