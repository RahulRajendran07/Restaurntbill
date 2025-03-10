from rest_framework import serializers
from rest.models import Category
class CategorySerializer(serializers.Serializer):

    class Mata:

        model = Category

        fields = "__all__"

        read_only_fields = ["id"]