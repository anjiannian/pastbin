# -*- coding: utf-8 -*-

from rest_framework import serializers
from django.contrib.auth.models import User

from snippets.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):

    """Docstring for SnippetSerializer. """
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.ModelSerializer):

    """Docstring for SnippetSerializer. """

    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')
