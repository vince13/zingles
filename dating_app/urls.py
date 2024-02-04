from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
# from profiles import urls as profile_urls
# from chat import urls as chat_urls
# from home import urls as home_urls
#
# from checkout import urls as subscribe_urls
# from search import urls as search_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('accounts/', include("profiles.urls")),
    path('chat/', include("chat.urls")),
    # path('subscribe/', include('subscribe.urls')),
    path('my-account/', include("account.urls")),
    path('search/', include("search.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
