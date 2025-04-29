from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Widget
from cdss_api.serializers import WidgetSerializer


# Create your views here.

class WidgetListView(APIView):
    """
    View to list all widgets in the system.
    """
    def get(self, request, lower_limit, higher_limit):
        """
        List all widgets in the system.
        """
        widgets = Widget.objects.filter(id__gte=lower_limit, id__lte=higher_limit)
        serializer = WidgetSerializer(widgets, many=True)
        print(serializer.data)
        return Response(serializer.data)

def NotFound(request, exception):
    return Response({"error": "Not Found"}, status=404)