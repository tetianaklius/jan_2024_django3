from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.cars.filter import CarFilter
# from apps.cars.filter import car_filter
from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer

# from core.paginations import PagePagination


class CarListCreateView(ListCreateAPIView):
    serializer_class = CarSerializer
    # pagination_class = PagePagination
    queryset = CarModel.objects.all()
    filterset_class = CarFilter

    # def get_queryset(self):
    #     return car_filter(self.request.query_params)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
