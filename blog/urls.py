from blog.views import *
from django.urls import path

from django.contrib import admin

app_name = 'blog' # namespace 에러가 발생할 때 자신의 urls.py에서 지정해야 한다

urlpatterns = [
    path('admin/', admin.site.urls),
    # /blog/
    path('post/Admincommunity2', saveDB, name='saveToDB'),

]

