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
        #  token = user.token
        # headers = {
        #     "Authorization": "Bearer YOUR_ACCESS_TOKEN"
        # }
        # self.client.get("/items/", headers=headers)

        self.client.get("/items/")

    @task
    def get_item(self):
        for item in Item.objects.all():
            self.client.get(f"/items/{item.pk}/")
