from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    # url(r'^$', 'anonconsearch.views.home', name='home'),
    # url(r'^anonconsearch/', include('anonconsearch.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'search.views.home'),
    url(r'^query/(?P<page_id>\d+)/$', 'search.views.query'),
    url(r'^query2/(?P<page_id>\d+)/$', 'search.views.query2')
)
