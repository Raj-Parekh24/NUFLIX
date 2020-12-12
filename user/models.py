from django.db import models
from .validators import file_size
# Create your models here.

class video(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to="videos/",validators=[file_size])
    def __str__(self) -> str:
        return self.name +" of subject "+self.subject
