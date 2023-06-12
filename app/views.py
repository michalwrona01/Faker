from rest_framework import status, views
from rest_framework.response import Response

from app.serializers import FakerRequestSerializer


class FakerView(views.APIView):
    """Fake view class"""
    def post(self, request):
        """Post method

        :param request: Request
        """
        serializer = FakerRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
