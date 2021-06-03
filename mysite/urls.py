from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls',),name="blog"),
    path('', TemplateView.as_view(template_name='base.html'), name="base")
]
