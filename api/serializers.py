from rest_framework import serializers
from .models import Cublista

class CublistaSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    #owner = serializers.ReadOnlyField(source='owner.username') # ADD THIS LINE
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Cublista
        fields = ('projeto', 'tipo', 'padrao', 'estado', 'mes', 'ano', 'valor') 
        #read_only_fields = ('date_created', 'date_modified')