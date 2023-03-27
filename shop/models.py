from django.db import models
from django.conf import settings
from django.urls import reverse
import uuid
# Create your models here.

class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return self.code



class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("shop:category_list", kwargs={'slug': self.slug})
    
class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("shop:tags_list", kwargs={'slug': self.slug})
    
class Item(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    photo = models.ImageField(upload_to="product/images/%Y/%m/%d")

    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    description = models.TextField()
    audio_fragments = models.FileField(upload_to='product/audio/%Y/%m/%d', null=True, blank=True)
    file = models.FileField(upload_to="product/files/%Y/%m/%d")
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL)

    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("shop:item_detail", kwargs={"slug": self.slug})
    
    def get_photo(self):
        if self.photo:
            return self.photo.url
        return ""
    
    
    def get_price(self):
        return self.price
    def get_discount_price(self):
        return self.discount_price
    def get_final_price(self):
        if self.discount_price:
            return self.get_discount_price()
        else:
            return self.get_price()

    class Meta:
        ordering = ['-created_at']

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, null=True, blank=True)
    items = models.ManyToManyField(Item)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    is_anonymous = models.BooleanField(default=True)
    coupon = models.ForeignKey(
        'Coupon', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_count(self):
        return self.items.count()
    
    def get_price_in_items(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        if self.coupon:
            total -= self.coupon.amount
        if self.user and self.user.discount > 0:
            total -= (total*self.user.discount)/100
        if total < 0: total = 0
        return total

    class Meta:
        ordering = ['-start_date']