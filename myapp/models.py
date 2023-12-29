from django.db import models

class Item(models.Model):
    title1 = models.CharField(max_length=255)
    title2 = models.CharField(max_length=255)
    image1 = models.ImageField(upload_to='item_images/')
    image2 = models.ImageField(upload_to='item_images/')
    time = models.DateTimeField()
    koef1 = models.FloatField()
    koef2 = models.FloatField()

    def __str__(self):
        return f"{self.title1} vs {self.title2}"
