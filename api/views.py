from rest_framework import viewsets
from django.core.cache import cache
from .models import Item
from .serializers import ItemSerializer
from rest_framework.response import Response


class ItemViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions (list, create, retrieve, update, destroy)
    for the Item model.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def list(self, request, *args, **kwargs):
        cached_items = cache.get('item_list')
        if cached_items is None:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            cache.set('item_list', serializer.data)
            return Response(serializer.data)
        return Response(cached_items)

    def retrieve(self, request, *args, **kwargs):
        instance = cache.get(f'item_{kwargs["pk"]}')
        if not instance:
            instance = self.get_object()
            cache.set(f'item_{kwargs["pk"]}', instance)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)