from django.conf.urls import include
from django.conf.urls import url

from django.contrib import admin

import djangae.urls

admin.autodiscover()

urlpatterns = [
    # Examples:
    #url(r'^$', 'testapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^_ah/', include(djangae.urls)),
    url(r'^auth/', include('djangae.contrib.gauth.urls')),
    url(r'^locking/', include('djangae.contrib.locking.urls')),
]
