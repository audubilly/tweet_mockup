from django.db import models


class TweetModel(models.Model):
    tweet = models.TextField(max_length=300, null=False, verbose_name='')
    tweet_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tweet

# Create your models here.
