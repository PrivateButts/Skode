from django.db import models


class CarouselItem(models.Model):
    image = models.ImageField(upload_to="carousel")
    alt = models.CharField(max_length=200, blank=True, null=True)
    caption = models.CharField(max_length=200, blank=True, null=True)
    button_label = models.CharField(max_length=200, blank=True, null=True)
    button_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.image.name
