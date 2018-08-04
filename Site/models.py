from django.db import models


class Price(models.Model):
    name = models.CharField(max_length=200)
    print_type = models.CharField(max_length=1, choices=(
        ('M', 'Matte Finish'),
        ('L', 'Luster Finish'),
        ('S', 'Semi Gloss Finish'),
        ('P', 'Platinum Finish'),
        ('F', 'Fine Art Smooth Finish'),
    ))
    print_size = models.CharField(max_length=10, choices=(
        ('8W', "8 Wallets (2.5 x 3.5)"),
        ('4x6', "4x6"),
        ('5x7', "5x7"),
        ('8x10', "8x10"),
        ('8.5x11', "8.5x11"),
        ('11x14', "11x14"),
        ('13x19', "13x19"),
    ))
    price = models.FloatField()

    def __str__(self):
        return self.name


class CarouselItem(models.Model):
    image = models.ImageField(upload_to="carousel")
    alt = models.CharField(max_length=200, blank=True, null=True)
    caption = models.CharField(max_length=200, blank=True, null=True)
    button_label = models.CharField(max_length=200, blank=True, null=True)
    button_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.image.name
