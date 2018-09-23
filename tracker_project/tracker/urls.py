from django.conf.urls import patterns, url
from tracker import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^bmi/$', views.bmi, name='bmi'),
        url(r'^weight/$', views.weight, name='weight'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        )
