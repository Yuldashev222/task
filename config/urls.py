from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from main.views import *

urlpatterns = [
    
    path('', include('main.urls')),

    path('admin/', admin.site.urls),
    
    path('api/signIn/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('api/signOut/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    path('api/signOut/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    
]