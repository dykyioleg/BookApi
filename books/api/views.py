from rest_framework import generics,mixins
from books.models import Book
from .serializers import BookSerializer
from .permissions import IsOwnerOrReadOnly


class BookAPIView(mixins.CreateModelMixin ,generics.ListAPIView): 
    lookup_field            = 'pk' 
    serializer_class        = BookSerializer
    

    def get_queryset(self):
        return Book.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BookRudView(generics.RetrieveUpdateDestroyAPIView): 
    lookup_field            = 'pk' 
    serializer_class        = BookSerializer
    permission_classes      = [IsOwnerOrReadOnly]
    

    def get_queryset(self):
        return Book.objects.all()