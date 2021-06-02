from django.urls import path

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
    path('doc/swagger/', views.schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc/redoc', views.schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

