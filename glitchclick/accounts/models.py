from django.db import models
from django.contrib.auth.models import User
from arts.models import *

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete = models.CASCADE)
    avatar = models.ImageField("Avatar", upload_to = "avatars/", default = "../static/images/no-avatar.png")
    favorites = models.ManyToManyField(Art)


    recomendations = models.TextField("Recomendation keywords", default="")
    girl_or_boy = models.CharField(max_length = 200, default = "")
    are_recomendations_are_ready = models.IntegerField("Are recomendations are ready?", default = 0)

    def __str__(self):
        return self.user.username