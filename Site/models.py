from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class CarouselItem(models.Model):
    image = models.ImageField(upload_to="carousel")
    alt = models.CharField(max_length=200, blank=True, null=True)
    caption = models.CharField(max_length=200, blank=True, null=True)
    button_label = models.CharField(max_length=200, blank=True, null=True)
    button_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.image.name


class Order(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    total = models.FloatField()

    def __str__(self):
        return f'Order #{self.pk}: ${self.total}'


class CartItem(models.Model):
    item_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name="cart_item_item")
    item_object_id = models.PositiveIntegerField()
    item_content_object = GenericForeignKey('item_content_type', 'item_object_id')

    category_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name="cart_item_category")
    category_object_id = models.PositiveIntegerField()
    category_content_object = GenericForeignKey('category_content_type', 'category_object_id')

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    price = models.FloatField()
    taxable = models.BooleanField(default=True)
    status = models.CharField(
        max_length=1,
        default='A',
        choices=(
            ('A', 'Active'),
            ('S', 'Sold')
        )
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        blank=True, null=True
    )

    @property
    def tax(self):
        if self.taxable:
            return self.price * settings.TAX_RATE
        else:
            return 0

    @property
    def total(self):
        return self.price + self.tax

    def __str__(self):
        return f'Cart item {self.category_content_object} in {self.user}\'s cart'
