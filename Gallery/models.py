from django.db import models
from sorl.thumbnail import ImageField


class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()

    featured = models.ForeignKey('Picture', blank=True, null=True, on_delete=models.SET_NULL, related_name="featured_set")
    
    def __str__(self):
        return "%s (%s)" % (self.name, self.date)


class Client(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    
    def __str__(self):
        return "%s <%s>" % (self.name, self.email)


class PricePoint(models.Model):
    name = models.CharField(max_length=200)
    print_type = models.CharField(max_length=200)
    print_size = models.CharField(max_length=200)

    price = models.FloatField()

    @property
    def formatted_price(self):
        return "${:.2f}".format(self.price)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    name = models.CharField(max_length=200)
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    unlisted = models.BooleanField(default=False)
    price_points = models.ManyToManyField(PricePoint, blank=True)

    def __str__(self):
        return self.name


class Picture(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    image = ImageField(upload_to="doggos")

    def __str__(self):
        return self.image.name
