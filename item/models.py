from django.db import models
from django.contrib.auth.models import User
from gdstorage.storage import GoogleDriveStorage

# Create your models here.
gd_storage = GoogleDriveStorage()


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Item(models.Model):
    # gd_storage = GoogleDriveStorage()

    category = models.ForeignKey(
        Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(
        upload_to='_PORJECT_', blank=True, null=True, storage=gd_storage)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
