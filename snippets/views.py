from rest_framework import viewsets
from rest_framework import renderers
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from django.contrib.auth.models import User

from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer, UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    List all the users
    Detail on specified user
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    '''
    List all the snippets
    Detail on specified snippet
    '''
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,
                        IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        """
        Save the owner of snippet while creating
        """
        serializer.save(owner=self.request.user)
