from ws.models import ValueArray
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from ws.serializers.value_array import ValueArraySerializer
from rest_framework.response import Response

from .functions import getArray

# This class is a view show all Values_array
class ValueList(generics.ListCreateAPIView):
    queryset = ValueArray.objects.all()
    serializer_class = ValueArraySerializer
    name = 'value-list'

    def post(self, request):
        try:
            data = request.data
            items = data['items']
            try:
                if isinstance(items, list):
                    items_result = getArray(items)
                    items_result.sort()
                    value_end = ValueArray()
                    value_end.data_input = items
                    value_end.data_output = items_result
                    value_end.ip = get_client_ip(request)
                    value_end.save()
                    return Response({'result': items_result}, status=200)
                else:
                    return Response({'The array input is not valid'}, status=404)
            except Exception as e:
                return Response({'The array input is not valid'}, status=404)
        except Exception as e:
            return Response({'BAD_REQUEST'}, status=status.HTTP_400_BAD_REQUEST)


# This class is a view show details of one Value
class ValueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ValueArray.objects.all()
    serializer_class = ValueArraySerializer
    name = 'value-detail'


def get_client_ip(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    except Exception as e:
        return ""