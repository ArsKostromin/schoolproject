from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from . import models
# Create your views here.

def index(request):
    context = {}
    return render(request, 'app_news/aboutUs.html', context)

class ProductListView(generic.ListView):
    model = models.Product
    paginate_by = 10
    



