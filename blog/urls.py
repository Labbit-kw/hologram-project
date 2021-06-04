from blog.views import *
from django.urls import path

app_name = 'blog' # namespace 에러가 발생할 때 자신의 urls.py에서 지정해야 한다

urlpatterns = [
    # /blog/
    path('post/Admincommunity2', saveDB, name='saveToDB'),

]

