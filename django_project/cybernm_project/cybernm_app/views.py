from django.shortcuts import render
from rest_framework import generics
from rest_framework.schemas import get_schema_view, openapi
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


class tournamentsListView(generics.ListAPIView):
    serializer_class = tournamentsListSeriallizer
    queryset = tournament.objects.all()


class playersListView(generics.ListAPIView):
    serializer_class = playersListSeriallizer
    queryset = User.objects.filter(is_staff=False)


class newsListView(generics.ListAPIView):
    serializer_class = newsListSeriallizer
    queryset = news.objects.all()


class disciplineListView(generics.ListAPIView):
    serializer_class = disciplineListSeriallizer
    queryset = discipline.objects.all()


class tournamentsRetrieveView(generics.RetrieveAPIView):
    serializer_class = tournamentsRetrieveSeriallizer
    queryset = tournament.objects.filter()


class PlayerRetrieveView(generics.RetrieveAPIView):
    serializer_class = PlayerRetrieveSeriallizer
    queryset = User.objects.filter(is_staff=False)


class nicknamesListView(generics.ListAPIView):
    serializer_class = nicknamesListSeriallizer
    queryset = User.objects.filter(is_staff=False)


class usersListView(generics.ListAPIView):
    serializer_class = usersListSeriallizer
    queryset = User.objects.filter(is_staff=False)


class DisciplineRetrieveView(generics.RetrieveAPIView):
    serializer_class = DisciplineRetrieveSeriallizer
    queryset = discipline.objects.filter()


class AddTournament(generics.CreateAPIView):
    serializer_class = tournamentsCreateSeriallizer


class AddDiscipline(generics.CreateAPIView):
    serializer_class = disciplineCreateSeriallizer


class tournamentsDesytoyView(generics.DestroyAPIView):
    serializer_class = tournamentsRetrieveSeriallizer
    queryset = tournament.objects.filter()


class tournamentsUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = tournamentsCreateSeriallizer
    queryset = tournament.objects.filter()


class disciplineDesytoyView(generics.DestroyAPIView):
    serializer_class = DisciplineRetrieveSeriallizer
    queryset = discipline.objects.filter()


class disciplineUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = disciplineCreateSeriallizer
    queryset = discipline.objects.filter()


class Addplayer(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = playerCreateSeriallizer


class playerDesytoyView(generics.DestroyAPIView):
    serializer_class = PlayerRetrieveSeriallizer
    queryset = User.objects.filter()


class playerUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = playerCreateSeriallizer
    queryset = User.objects.filter()


schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='v2',
      description="Description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="hardbeat34@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)