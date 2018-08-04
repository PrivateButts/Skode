from django.db import models


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


class Gallery(models.Model):
    name = models.CharField(max_length=200)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Picture(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="doggos")

    def __str__(self):
        return self.image.name
