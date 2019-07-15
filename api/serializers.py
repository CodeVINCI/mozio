from rest_framework_mongoengine import serializers as mongoserializers
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer

from .models import Provider,Polygon,User

class ProviderSerializer(mongoserializers.DocumentSerializer):
    class Meta:
        model = Provider
        fields = ('name','phone_number','currency','language')


class ProviderSelectSerializer(mongoserializers.DocumentSerializer):
    class Meta:
        model = Provider
        fields = ('name','currency')


class PolygonSerializer(mongoserializers.DocumentSerializer):
    provider = ProviderSelectSerializer()
    class Meta:
        model = Polygon
        depth = 1
        fields = ('name','provider','polygon')


class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField(label=_("Username"))
    password = serializers.CharField(label=_("Password"), style={'input_type': 'password'})

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if user:
                # From Django 1.10 onwards the `authenticate` call simply
                # returns `None` for is_active=False users.
                # (Assuming the default `ModelBackend` authentication backend.)
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError(msg)
            else:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg)
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg)

        attrs['user'] = user
        return attrs
