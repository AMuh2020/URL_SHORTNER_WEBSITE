from django.db import models

# Create your models here.
class Urls(models.Model):
    url = models.CharField(max_length=200)
    url_short = models.CharField(max_length=100, default='j')
    visits = models.PositiveIntegerField(default=0)
    pub_date = models.DateTimeField('date last modified')
    def __str__(self):
        return self.url
