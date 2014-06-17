from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
'''admin login: admin / ciseau '''

from tastypie.api import Api
from polls.api import PollResource, ChoiceResource
 
v1_api = Api(api_name='v1')
v1_api.register(PollResource())
v1_api.register(ChoiceResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^oauth2/', include('provider.oauth2.urls', namespace = 'oauth2')),    
    url(r'^api/', include(v1_api.urls)),
)
