from django.db import models


class House(models.Model):
    name = models.CharField("title", max_length=50)
    price = models.IntegerField("price")
    description = models.TextField("description")
    photo = models.ImageField("photo", upload_to="houses/photos", default="", blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
