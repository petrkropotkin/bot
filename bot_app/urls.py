from django.conf.urls import url
from bot_app import views

urlpatterns = [
url(r'^$',views.index, name='index'),

]
