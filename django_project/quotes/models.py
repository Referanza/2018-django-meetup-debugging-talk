import re

from django.db import models

class Author(models.Model):
    SLUGIFY = re.compile(r'\W') # Match any non-word character

    name = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.SLUGIFY.sub("-", self.name.lower())

        return super().save(*args, **kwargs)

class Quote(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.TextField()

import django_extensions.management.commands.runserver_plus
