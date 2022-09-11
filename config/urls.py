from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt import views as jwt_views
from main.views import *


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
    openapi.Info(
        title="Jaseci API",
        default_version='v1',
        description="Welcome to the world of Jaseci",
        terms_of_service="https://www.jaseci.org",
        contact=openapi.Contact(email="jason@jaseci.org"),
        license=openapi.License(name="Awesome IP"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),

    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'),
    
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),
    
    path('', include('main.urls')),

    path('admin/', admin.site.urls),
    
    path('api/signIn/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('api/signOut/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    path('api/signOut/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    
]