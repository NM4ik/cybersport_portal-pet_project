from django.urls import path, include, re_path

from cybernm_project import settings
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("Alltournaments/", views.tournamentsListView.as_view()),
    path("Allplayers/", views.playersListView.as_view()),
    path("Alldisciplines/", views.disciplineListView.as_view()),
    path("Allnews/", views.newsListView.as_view()),
    path("Onetournament/<int:pk>/", views.tournamentsRetrieveView.as_view()),
    path("Oneplayer/<pk>/", views.PlayerRetrieveView.as_view()),
    path("Onediscipline/<int:pk>/", views.DisciplineRetrieveView.as_view()),
    path("Addtournament/", views.AddTournament.as_view()),
    path("Deletetournament/<int:pk>/", views.tournamentsDesytoyView.as_view()),
    path("Updatetournament/<int:pk>/", views.tournamentsUpdateView.as_view()),
    path("Adddiscipline/", views.AddDiscipline.as_view()),
    path("Deletediscipline/<int:pk>/", views.disciplineDesytoyView.as_view()),
    path("Updatediscipline/<int:pk>/", views.disciplineUpdateView.as_view()),
    path("Addplayer/", views.Addplayer.as_view()),
    path("Deleteplayer/<int:pk>/", views.playerDesytoyView.as_view()),
    path("Updateplayer/<pk>/", views.playerUpdateView.as_view()),
    path("nicknames", views.nicknamesListView.as_view()),
    path("users", views.usersListView.as_view()),
    path("auth/", include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('doc/swagger/', views.schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc/redoc', views.schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

