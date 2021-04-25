"""
Map of GVZ URLs to views
"""
# pylint: disable=R0903

from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import AdministrativeDivision, ZipCode
from .views import index

class AdministrativeDivisionSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialize the AdministrativeDivision model
    """
    class Meta:
        """
        Define serialized fields
        """
        model = AdministrativeDivision
        # fields = '__all__'
        fields = ['ags', 'name', 'parent', 'children', 'division_category', 'division_type', 'office_zip', 'office_street', 'office_city',
                  'area', 'citizens_total', 'citizens_male', 'citizens_female', 'population_density', 'longitude', 'latitude', 'travel_name', 'travel_code']

class AdministrativeDivisionViewSet(viewsets.ModelViewSet):
    """
    Define AdministrativeDivision view set (return all)
    """
    queryset = AdministrativeDivision.objects.all()
    serializer_class = AdministrativeDivisionSerializer
    filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['ags', 'name', 'parent', 'division_type', 'division_category']

class ZipCodeSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialize the ZipCode model
    """
    class Meta:
        """
        Define serialized fields
        """
        model = ZipCode
        fields = '__all__'

class ZipCodeViewSet(viewsets.ModelViewSet):
    """
    Define ZipCode view set (return all)
    """
    queryset = ZipCode.objects.all()
    serializer_class = ZipCodeSerializer

router = routers.DefaultRouter()  # pylint: disable=C0103
router.register(r'administrative_divisions', AdministrativeDivisionViewSet)
router.register(r'zip_codes', ZipCodeViewSet)

urlpatterns = [  # pylint: disable=C0103
    path('', index),
    path('api/', include(router.urls))
]
