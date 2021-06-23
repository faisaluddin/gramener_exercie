from rest_framework.response import Response
from rest_framework import viewsets, status
from django.conf import settings

from .models import Math
from .serializers import MathSerializer


class MathViewset(viewsets.ModelViewSet):
    queryset = Math.objects.all()
    serializer_class = MathSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        path = settings.BASE_DIR / (request.data['operation_name']+'.py')
        with open(path, 'w') as file:
            file.write(request.data['func'].lstrip())
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        module = __import__(instance.operation_name)

        params = [int(x) for x in request.GET.keys()]
        output = 0
        try:
            output = getattr(module, str(instance.operation_name))(*params)
        except Exception as e:
            output = str(e)
        return Response({'output': output})

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        path = settings.BASE_DIR / (request.data['operation_name']+'.py')
        with open(path, 'w') as file:
            file.write(request.data['func'].lstrip())

        self.perform_update(serializer)
        return Response(serializer.data)
