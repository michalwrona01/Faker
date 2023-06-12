from faker import Faker
from rest_framework import serializers


class FakerRequestSerializer(serializers.Serializer):
    """Faker request serializer class"""

    first_name = serializers.BooleanField(required=False)
    last_name = serializers.BooleanField(required=False)
    city = serializers.BooleanField(required=False)
    street_address = serializers.BooleanField(required=False)
    date_of_birth = serializers.BooleanField(required=False)
    zipcode = serializers.BooleanField(required=False)
    email = serializers.BooleanField(required=False)
    pesel = serializers.BooleanField(required=False)
    url = serializers.BooleanField(required=False)
    phone_number = serializers.BooleanField(required=False)

    def to_representation(self, instance):
        """Returns random data"""

        fake = Faker(["pl_PL"])
        self.is_valid(raise_exception=True)
        response_data = {}
        for field_name in self.fields.keys():
            if self.validated_data.get(field_name, field_name):
                response_data.update({field_name: getattr(fake, field_name)()})
        return response_data
