from django.db import models

class NewsFeed(models.Model):
    url_input = models.CharField(max_length=100)

    def __str__(self):
        return self.url_input
