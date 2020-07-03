from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=256)
    slug = models.CharField(max_length=256, unique=True)
    image = models.ImageField()

    def __str__(self):
        return self.title


class Chapter(models.Model):
    number = models.CharField(max_length=16, unique=True)
    title = models.CharField(max_length=256)
    slug = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class Section(models.Model):
    number = models.CharField(max_length=16)
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class Fragment(models.Model):
    number = models.CharField(max_length=16)
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title
