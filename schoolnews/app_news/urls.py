from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView


urlpatterns = [
    path('AboutUs', views.index, name='index'),
    path('', views.ProductListView.as_view(), name='news'),
    path('rubric<int:pk>', views.RubricDetailView.as_view(), name='rubric_detail'),
    path('<pk>', views.ProductDetailView.as_view(), name='detail_product'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.SignUp.as_view(), name="signup"),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''urlpatterns += [
    path('rubric<int:pk>', views.RubricDetailView.as_view(), name='rubric_detail'),
]'''