from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = "Yangiliklar"

    def __str__(self):
        return self.title
