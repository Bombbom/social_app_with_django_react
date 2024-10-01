from rest_framework import serializers 
class AbstractSerializer(serializers.ModelSerializer):
    """
    AbstractSerializer from rest_framework.serializers.ModelSerializer.
    * Fields: id from public_id, created, updated.
    * .create(), .update()
    """
    id = serializers.UUIDField(source='public_id', read_only=True, format='hex')
    
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
    