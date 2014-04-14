from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'note.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^register.html$','mynote.views.register'),
    url(r'^login$','mynote.views.login'),
    url(r'^note_manage$','mynote.views.note_manage'),
    url(r'^note_add$','mynote.views.note_add'),
    url(r'^captcha/', include('captcha.urls')),
)
