from dataclasses import field
from rest_framework import serializers

from user.models import (
    User
)

# ----------------------------------------------------------------------
#  Serializers
# ----------------------------------------------------------------------

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

