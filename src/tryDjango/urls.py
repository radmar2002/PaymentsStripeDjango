from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'profiles.views.home', name='home'),
    url(r'^about/$', 'profiles.views.about', name='about'),
    url(r'^contact/$', 'contact.views.contact', name='contact'),
    # url(r'^blog/', include('blog.urls')),

    
]


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)