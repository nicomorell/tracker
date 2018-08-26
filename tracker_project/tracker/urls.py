from django.conf.urls import patterns, url
from tracker import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^bmi/$', views.bmi, name='bmi'),
        url(r'^weight/$', views.weight, name='weight'))
