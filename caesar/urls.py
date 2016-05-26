from django.conf.urls import url

from . import views

app_name = 'caesar'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^encode/$', views.handler, name='encode'),
    url(r'^decode/$', views.handler, name='decode'),
    url(r'^history/$', views.HistoryView.as_view(), name='history'),
]