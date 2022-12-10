from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from . import models
from .forms import CommentForm
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    context = {}
    return render(request, 'app_news/aboutUs.html', context)

class ProductListView(generic.ListView):
    model = models.Product
    paginate_by = 10

   


class ProductDetailView(generic.DetailView):
    model = models.Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        
        form = CommentForm()
        product = get_object_or_404(models.Product, pk=pk)
        comments = product.comments.all()

        context['product'] = product
        context['comments'] = comments
        context['form'] = form
        return context

    def product(self, request, *args, **kwargs):
        form = CommentForm(request.PRODUCT)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)

        product = models.Product.objects.filter(id=self.kwargs['pk'])[0]
        comments = product.comments.all()

        context['product'] = product
        context['comments'] = comments
        context['form'] = form

        if form.is_valid():
            body = form.cleaned_data[body]
            user = form.cleaned_data[user]
            comment = models.Comment.objects.create(body = body, product=product, user=user)
        
            form = CommentForm()
            context['form'] = form 
            return self.render_to_response(context=context)
        
        return self.render_to_response(context=context)

    




