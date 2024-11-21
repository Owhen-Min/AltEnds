from django.urls import path, include
from accounts import views

urlpatterns = [
    path('api/v1/accounts/', include('dj_rest_auth.urls')),
    path('api/v1/accounts/signup/', include('dj_rest_auth.registration.urls')),
    path('api/v1/movies/', include('moviearticles.urls')),
    path('api/v1/communities/', include('communityarticles.urls')),
    path('api/v1/accounts/<int:user_pk>/', views.GetProfile),
]
