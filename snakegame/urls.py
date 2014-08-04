from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'snake.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^snake/$', 'snake.views.snake', name='snake'),

    # User Registration
    url(r'^register/$', 'snake.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),

    # Save Game
    url(r'^save/$', 'snake.views.save', name='save'),
    url(r'^profile/$', 'snake.views.profile', name='profile'),
    url(r'^leaderboard/$', 'snake.views.leaderboard', name='leaderboard'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
