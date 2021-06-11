from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from .models import *


class tournamentsListSeriallizer(serializers.ModelSerializer):
    # discipline_id = serializers.SlugRelatedField(slug_field="discipline_name", read_only=True)

    class Meta:
        model = tournament
        fields = "__all__"

    status = serializers.CharField(source='get_status_display')
    limitation = serializers.CharField(source='get_limitation_display')


class disciplineListSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = discipline
        fields = "__all__"


class newsListSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = news
        fields = "__all__"


class playersListSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = player
        fields = "__all__"


class nicknamesListSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = player
        fields = ("nickname",)


class tournamentsCreateSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = tournament
        fields = "__all__"

    def create(self, validated_data):
        savetournaments = tournament(**validated_data)
        savetournaments.save()
        return savetournaments


class disciplineCreateSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = discipline
        fields = "__all__"

    def create(self, validated_data):
        savediscipline = discipline(**validated_data)
        savediscipline.save()
        return savediscipline


class tournamentsRetrieveSeriallizer(serializers.ModelSerializer):
    discipline_id = serializers.SlugRelatedField(slug_field="discipline_name", read_only='True')
    players = playersListSeriallizer(many=True, read_only=True)

    class Meta:
        model = tournament
        fields = "__all__"

    status = serializers.CharField(source='get_status_display')
    limitation = serializers.CharField(source='get_limitation_display')


class PlayerRetrieveSeriallizer(serializers.ModelSerializer):
    tournament_player = tournamentsListSeriallizer(many=True, read_only=True)

    class Meta:
        model = player
        fields = "__all__"


class DisciplineRetrieveSeriallizer(serializers.ModelSerializer):

    class Meta:
        model = discipline
        fields = "__all__"


class playerCreateSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = player
        fields = "__all__"

    def create(self, validated_data):
        saveplayer = player(**validated_data)
        saveplayer.save()
        return saveplayer



