from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
