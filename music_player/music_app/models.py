from django.db import models

# Create your models here.
from django_extensions.db.models import TimeStampedModel,TitleDescriptionModel

from django.core.validators import FileExtensionValidator

class Song(TimeStampedModel,TitleDescriptionModel):

    music = models.FileField(upload_to="audio", validators=[FileExtensionValidator(allowed_extensions=['mp3'])])
    artist=models.CharField(max_length=100,null=False,blank=False)
    poster=models.ImageField(upload_to ='image',max_length=100,null=False,blank=False)

    class Meta:
	    verbose_name = "Song"
	    verbose_name_plural = "Songs"


class Video(TimeStampedModel,TitleDescriptionModel):

    video = models.FileField(upload_to="video_player/video", validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    artist=models.CharField(max_length=100,null=False,blank=False)
    poster=models.ImageField(upload_to ='video_player/img',max_length=100,null=False,blank=False)

    class Meta:
	    verbose_name = "Video"
	    verbose_name_plural = "Videos"


class RelatedSimilar(TimeStampedModel,TitleDescriptionModel):
    relatedsimilar = models.ForeignKey(Video,  related_name='relatedsimilars', on_delete=models.CASCADE)


    def __str__(self):
    	return self.relatedsimilar

class Mostwatch(TimeStampedModel,TitleDescriptionModel):
    mostwatch = models.ForeignKey(Video,  related_name='mostwatchs', on_delete=models.CASCADE)

    def __str__(self):
    	return self.title