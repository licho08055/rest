from dataclasses import fields
from rest_framework import serializers
from api_base.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        #fields=['id', 'title', 'author',]
        fields='__all__'