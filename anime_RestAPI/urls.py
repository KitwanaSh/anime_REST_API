from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
    )

from django.conf.urls.static import static
from anime_RestAPI import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger/', SpectacularSwaggerView.as_view(), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('sonar/', include('django_sonar.urls')),


    # API ENDPOINTS
    path('auth/', include('djoser.urls')),
    path('jwt/', include('djoser.urls.jwt')),


    # APPLICATION ENDPOINTS
    path('api/', include('google_login.urls')),
    path('merchant_profile/', include('profiles.urls')),
    path('products/', include('products.urls')),
    path('notifications/', include('notifications.urls')),
]
