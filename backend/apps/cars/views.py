from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.cars.filter import CarFilter
from apps.cars.models import CarModel
from apps.cars.serializers import CarPhotoSerializer, CarSerializer


class CarListView(ListAPIView):
    """
    Get all cars
    """
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    filterset_class = CarFilter
    permission_classes = (AllowAny,)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    get:
        get car details
    put:
        update car
    patch:
        partial update car
    delete:
        delete car
    """

    serializer_class = CarSerializer
    queryset = CarModel.objects.all()

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return (IsAuthenticated(),)
        return (AllowAny(),)


class CarAddPhotoView(UpdateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CarPhotoSerializer
    queryset = CarModel.objects.all()
    http_method_names = ('put',)

    def perform_update(self, serializer):
        car = self.get_object()
        car.photo.delete()
        super().perform_update(serializer)

# class TestEmailView(GenericAPIView):
#     permission_classes = (AllowAny,)
#     def get(self, *args, **kwargs):
#         EmailService.send_test()
#         return Response(status=status.HTTP_200_OK)
