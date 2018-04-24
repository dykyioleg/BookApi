from rest_framework import serializers
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = [
            'pk',
            'author',
            'title',
            'description',
            'timestamp',
        ]
        read_only_fields = ['pk', 'author']

    def validate_title(self, value):
        qs = Book.objects.filter(title__iexact=value) 
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("This title has already been used")
        return value
            