from django.conf.urls import patterns, include, url

urlpatterns = patterns('myapp.views',
   url(r'^hello/', 'hello', name = 'hello'),
   url(r'^projet/', 'projet', name = 'projet'),)

