from django.db import models

# Create your models here.
class News(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	author = models.CharField(max_length=100)
	img = models.ImageField(upload_to='news_images/', blank=True, null=True)
	class Meta:
		
		ordering = ['-created_at']
		verbose_name = 'News'
		verbose_name_plural = 'News'
	def __str__(self):
		return self.title

class Player(models.Model):
	name = models.CharField(max_length=100)
	age = models.IntegerField()
	country = models.CharField(max_length=100)
	Rank = models.IntegerField()
	photo = models.ImageField(upload_to='player_photos/', blank=True, null=True)
	class Meta:
		ordering = ['name']
		verbose_name = 'Player'
		verbose_name_plural = 'Players'

	def __str__(self):
		return self.name