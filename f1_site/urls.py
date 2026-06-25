from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('drivers/', include('drivers.urls')),
    path('teams/', include('teams.urls')),
    path('circuits/', include('circuits.urls')),
    path('seasons/', include('seasons.urls')),
    path('records/', include('records.urls')),
    path('terminology/', include('terminology.urls')),
    path('halloffame/', include('halloffame.urls')),
    path('tyres/', include('tyres.urls')),
]

# Serve media files in production too
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)