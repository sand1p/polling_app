from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import permission_classes
# Create your views here.
# Response takes unrendered content and uses content negotiation to determine correct
# content type to the client

@permission_classes((permissions.AllowAny, ))
class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        """
        List all code snippets, or create a new Snippet.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # snippet serializer accepts python instance
        return self.create(request, *args, **kwarg)


@permission_classes((permissions.AllowAny,))
class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    """
    Retrieve, update or delete a code snippet.
    """
    queryset =Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(self, request, *args, **kwargs)

    def put(self, request,*args,**kwargs):
        return self.update(self,request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args,**kwargs)


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

