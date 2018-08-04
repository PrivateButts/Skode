from .models import Event


def nav_events(http):
    return {
        "EVENTS": Event.objects.all().order_by('name')
    }