from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView


urlpatterns = [
    path('AboutUs', views.index, name='index'),
    path('', views.ProductListView.as_view(), name='news'),
    path('<int:pk>', views.ProductDetailView.as_view(), name='detail_product')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

