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
        print(module.__dict__)

        qp = request.GET
        params = []
        for p in qp:
            params.append(int(qp[p]))
        output = 0
        try:
            output = getattr(module, str(instance.operation_name))(*params)
        except TypeError as e:
            output = str(e)
        return Response({'output': output})
