from django.db import models


class File(models.Model):
    file = models.FileField(blank=False, null=False)
    caption = models.CharField(max_length=500,default="")
    like = models.IntegerField(default=0)
    def __str__(self):
        return self.file.name
