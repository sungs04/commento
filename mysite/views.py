from django.shortcuts import render
from .models import MainContent
# Create your views here.
def index(request):
    content_list=MainContent.objects.order_by('-pub_date')
    context={'content_list': content_list}
    return render(request, 'mysite/content_list.html', context)

def introduce(request):
    introduce=MainContent.objects.order_by('-pub_date')
    context={'introduce': introduce}
    return render(request, 'mysite/introduce.html', context)

def products(request):
    products=MainContent.objects.order_by('-pub_date')
    context={'introduce': products}
    return render(request, 'mysite/products.html', context)

def ETX(request):
    ETX=MainContent.objects.order_by('-pub_date')
    context={'introduce': ETX}
    return render(request, 'mysite/ETX.html', context)