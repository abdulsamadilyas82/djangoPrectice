from rest_framework import serializers
from .models import Books

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        # fields = ['title', 'author', 'published_date', 'isbn']
        fields = '__all__'