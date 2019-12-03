from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Knot(models.Model):
    name = models.CharField(max_length=100, unique=True,
            blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True,
            blank=True, null=True)
    # description text field
    # images foreign key to KnotImage model
    # movies foreign key to KnotMovie model

    def __str__(self): 
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Knot, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('knot-detail', kwargs={'slug': self.slug})


class AlternativeName(models.Model):
    name = models.CharField(max_length=100, unique=False,
            blank=True, null=True)
    knot = models.ForeignKey(Knot, on_delete=models.CASCADE)

    def __str__(self): 
        return self.name

"""
class KnotImage(models.Model):
    file_path = ??
    name = models.CharField(max_length=100, unique=True,
            blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True,
            blank=True, null=True)
"""
