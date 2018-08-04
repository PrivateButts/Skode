from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    
    def __str__(self):
        return "%s (%s)" % (self.name, self.date)


class Client(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    
    def __str__(self):
        return "%s <%s>" % (self.name, self.email)


class Picture(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="doggos")

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
