from django.urls import path, include, re_path

from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('search', views.search, name='search'),
    re_path(r'^advanced-search$', views.advanced_search, name='advanced_search'),
    path('sample/<uuid:sample_id>', views.sample_detail, name='sample_detail'),
    path('sample/<uuid:sample_id>/csv', views.sample_detail_export, name='sample_detail_export'),
    path('sample/<uuid:sample_id>/favorite', views.sample_favorite, name='sample_favorite'),
]
