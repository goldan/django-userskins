from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^set/$', 'userskins.views.set', name = 'userskins_set'),
)

