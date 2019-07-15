from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework_mongoengine.viewsets import GenericViewSet,ModelViewSet as MongoModelViewSet
from rest_framework.response import Response
from .models import Provider,Polygon
from .serializers import ProviderSerializer, PolygonSerializer, AuthTokenSerializer
from .authentication import TokenAuthentication
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils.crypto import get_random_string
# Create your views here.



class Getproviders(MongoModelViewSet):
    lookup_field = 'id'
    serializer_class = ProviderSerializer

    def get_queryset(self):
        return Provider.objects.all()



class GetPolygons(MongoModelViewSet):

    lookup_field = 'id'
    serializer_class = PolygonSerializer

    def get_coordinates(self):
        coordinates={}
        coordinates['lat'] = float(self.request.query_params.get('lat'))
        coordinates['lng'] = float(self.request.query_params.get('lng'))
        return coordinates

    def get_queryset(self):
        coordinates = self.get_coordinates()
        geolocation = {"type": "Point", "coordinates": [coordinates['lng'], coordinates['lat']]}
        return Polygon.objects(polygon__geo_intersects=geolocation)


class CreateProvider(APIView):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.data.get('_content',''))
        name = data.get('name',"")
        email = data.get('email',"")
        phone_number = data.get('phone_number',"")
        currency = data.get("currency","")
        language = data.get("language","")
        unique_id = get_random_string(length=32)
        p = Provider(token=unique_id,name=name,email=email,phone_number=phone_number,currency=currency,language=language)
        p.save()
        return Response({"token":p.token})
    def get(self, request,*args,**kwargs):
        return Response({"success":1})

class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    authentication_classes = (TokenAuthentication, )
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

def index_view(request):
    context = {}
    return TemplateResponse(request, 'index.html', context)
