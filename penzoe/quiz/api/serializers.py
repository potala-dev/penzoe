from rest_framework import serializers


class FBSerializer(serializers.Serializer):
    """Fill-in-the-Blank serializer."""

    left_context = serializers.CharField()
    right_context = serializers.CharField()
    choices = serializers.ListField(child=serializers.CharField())
    correct_choice = serializers.CharField()
