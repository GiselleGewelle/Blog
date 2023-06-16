from django.db import models

from posts.models import Post


# Create your models here.
class Like(models.Model):
    owner = models.ForeignKey('auth.user', related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['owner', 'post']


class Favorite(models.Model):
    owner = models.ForeignKey('auth.user', related_name='favorites', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='favorites', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['owner', 'post']