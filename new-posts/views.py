from django.shortcuts import render
from django.db import models


class Headline(models.Model):
    """ Scrape data from websites

    The posts will contain images, url's and titles.
    models - headline(title, image, url)
    """
    title = models.CharField(max_length=200)
    image = models.URLField(null=True, blank=True)
    url = models.TextField()

    def __str__(self):
        return self.title
