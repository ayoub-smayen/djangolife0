from rest_framework import serializers

from . import models


class ProductSerializer(serializers.ModelSerializer):
    #permission_classes = (permissions.AllowAny,)
    class Meta:
        model = models.Product
        fields = ('__all__')