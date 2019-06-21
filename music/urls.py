
from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    path('', views.index, name='index'),

    # /music/712/
    path('<int:album_id>', views.detail, name='detail'),

    # /music/712/favorite
    path('<int:album_id>/favorite/', views.favorite, name='favorite'),
]
