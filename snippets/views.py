from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
# Create your views here.
# Response takes unrendered content and uses content negotiation to determine correct
# content type to the client

@permission_classes((permissions.AllowAny, ))
class SnippetList(APIView):
    def get(request, format=None):
        """
        List all code snippets, or create a new Snippet.
        """
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(request, format=None):
        # snippet serializer accepts python instance
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((permissions.AllowAny,))
class SnippetDetail(APIView):
    """
    Retrieve, update or delete a code snippet.
    """
    def get_object(self, pk):
        try:
            snippet = Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@permission_classes((permissions.AllowAny, ))
def get_latest_snippets(request, hours):
    """
    Return those snippets that are created very recently.
    hours: no of hours from creation of the snippet
    """
    from_date = datetime.now() - datetime.hour
    queryset = Snippet.objects.filter(created__range=[from_date, to_date])
    serializer = SnippetSerializer(queryset, many=True)
    return Response(serializer.data)

