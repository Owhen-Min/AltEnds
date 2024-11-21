from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/altends/', views.generate_alt_ending),
    path('altends/', views.ending_list),
    path('altends/<int:ending_pk>/', views.ending_detail),
    path('altends/<int:ending_pk>/comments/', views.comment_list),
    path('altends/<int:ending_pk>/likes/', views.likes),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)