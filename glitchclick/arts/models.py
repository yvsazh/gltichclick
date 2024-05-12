from django.db import models

from django.contrib.auth.models import User


class Art(models.Model):
    keywords = models.CharField("keywords", max_length = 500)
    image = models.ImageField("Art", upload_to = "arts/")
    views = models.IntegerField("Views", default = 0)
    saved = models.IntegerField("Saved", default = 0)

    genders = (
        ('girl', 'girl'),
        ('boy', 'boy'),
    )

    gender = models.CharField("Gender", max_length = 20, choices = genders, default="girl")

    def __str__(self):
        return self.keywords

    class Meta:
        verbose_name = "Art"
        verbose_name_plural = "Arts"

from accounts.models import *

class Comment(models.Model):
    art = models.ForeignKey(Art, on_delete = models.CASCADE)
    author = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    text = models.CharField("Text", max_length = 1000)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"