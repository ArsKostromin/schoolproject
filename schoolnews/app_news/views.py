from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from . import models
from .forms import CommentForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect
from schoolnews.settings import AUTH_USER_MODEL
from django.views.generic.edit import FormMixin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth  import get_user_model


# Create your views here.

def index(request):
    context = {}
    return render(request, 'app_news/aboutUs.html', context)

class ProductListView(generic.ListView):
    model = models.Product
    paginate_by = 3

class RubricDetailView(generic.DetailView):
    model = models.Rubric



class ProductDetailView(FormMixin, generic.DetailView):
    model = models.Product
    form_class = CommentForm

    def get_success_url(self):
        return reverse('detail_product', kwargs={'pk': self.get_object().id})

    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.product = self.get_object()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
        
        





