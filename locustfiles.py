import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "www.settings")

import django
django.setup()


import time
from locust import HttpUser, task, between
from api.models import Item


total_items = Item.objects.count()

class Items(HttpUser):
    wait_time = between(1, 2)

    @task
    def get_items(self):
        self.client.get("/items/")

    @task
    def get_item(self):
        for item_id in range(1, total_items + 1):
            self.client.get(f"/items/{item_id}/")
