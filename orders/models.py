from django.db import models
from houses.models import House


class Order(models.Model):
    house = models.ForeignKey(House, verbose_name="house")
    name = models.CharField("name", max_length=50)
    phone = models.CharField("phone", max_length=50)
    date = models.DateTimeField("Date", auto_now_add=True)
