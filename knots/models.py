from django.db import models
from django.utils.text import slugify



class Knot(models.Model):
    name = models.CharField(max_length=100, unique=True,
            blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True,
            blank=True, null=True)

    def __str__(self): 
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Knot, self).save(*args, **kwargs)
