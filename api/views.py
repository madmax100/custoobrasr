from rest_framework import generics

from .models import Cublista
#from .permissions import IsOwner

from .serializers import CublistaSerializer


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Cublista.objects.all()
    queryset = queryset.filter(ano=2018).filter(mes='janeiro 2018').filter(estado='Ceará')

    serializer_class = CublistaSerializer
    #permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

