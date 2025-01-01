from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Item


@receiver(post_save, sender=Item)
def invalidate_cache_on_save(sender, instance, **kwargs):
    print('Invalidating cache on create or update')
    # Invalidate the cache for the item list
    cache.delete('item_list')
    cache.delete(f'item_{instance.id}')

@receiver(post_delete, sender=Item)
def invalidate_cache_on_delete(sender, instance, **kwargs):
    print('Invalidating cache on delete')
    # Invalidate the cache for the item list
    cache.delete('item_list')
    cache.delete(f'item_{instance.id}')
