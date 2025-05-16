from rest_framework import serializers


class WidgetSerializer(serializers.Serializer):
    """
    Serializer for Widget model.
    """
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    downloads = serializers.IntegerField()
    publishDate = serializers.DateTimeField()
    # def create(self, validated_data):
    #     """
    #     Create a new widget instance.
    #     """
    #     return Widget.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """
    #     Update an existing widget instance.
    #     """
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.value = validated_data.get('value', instance.value)
    #     instance.save()
    #     return instance