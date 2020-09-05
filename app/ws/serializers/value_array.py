from rest_framework import serializers
from ws.models import ValueArray


class ValueArraySerializer(serializers.ModelSerializer):

    class Meta:
        model = ValueArray
        fields = (
            'id',
            'created_date',
            'data_input',
            'data_output',
            'ip',
        )
        read_only_fields = (
            'id',
        )
