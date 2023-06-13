from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.serializers import FakerSerializer


class FakerView(views.APIView):
    """Fake view class"""

    serializer = FakerSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    @swagger_auto_schema(request_body=FakerSerializer)
    def post(self, request):
        """Send request which fields you want to get.
        If you sent nothing you get all fields."""

        serializer = FakerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
