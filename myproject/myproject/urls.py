from django.conf.urls import patterns, include, url
from django.contrib import admin
from polls.views import hello,questions,current_datetime,choices

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^hello/$',hello),
    url(r'^questions/$',questions),
    url(r'^questions/(?P<question_id>\d+)/choices/$',choices),
    url(r'^current_datetime/$',current_datetime),
    url(r'^admin/', include(admin.site.urls)),
)
