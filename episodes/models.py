from django.db import models
from django import forms
from ckeditor.fields import RichTextField

# Create your models here.
class Episode(models.Model):
	created_at = models.DateTimeField(auto_now=True)
	title = models.CharField(max_length=255)
	number = models.CharField(max_length=3)
	info = RichTextField()
	image = models.ImageField(upload_to='episodes/images/',
		max_length=500, default='assets/not-found.jpg')
	audio = models.FileField(upload_to='episodes/audio/',
		max_length=500, default='assets/not-found.mp3')
	active = models.BooleanField(default=True)

	class Meta:
		ordering = ['-number',]

	def __str__(self):
		return self.title
