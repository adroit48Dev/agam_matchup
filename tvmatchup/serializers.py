from rest_framework import serializers
from .models import Matchup, Templates


class MatchupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
                  'matchup_id',
                  'image',
                  'keyword',
                  'description',
                  'created_at'

                  )
        model = Matchup


class TemplateSerializer(serializers.ModelSerializer):
    lists = MatchupSerializer(many=True, read_only=True)

    class Meta:
        fields = ('temp_name', 'templ_id', 'lists',)
        model = Templates
