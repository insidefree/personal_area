from django.db import models


class House(models.Model):
    name = models.CharField("title", max_length=50)
    price = models.IntegerField("price")
    description = models.TextField("description")
