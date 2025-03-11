from rest_framework import serializers
from rest.models import Category,Item
class CategorySerializer(serializers.ModelSerializer):

    class Meta:

        model = Category

        fields = "__all__"

        read_only_fields = ["id"]


class ItemSerializer(serializers.ModelSerializer):

    class Meta :

        model = Item

        fields = "__all__"

        read_only_fields = ["id","category_object"]
