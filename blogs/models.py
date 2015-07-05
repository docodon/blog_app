from django.db import models

# Create your models here.
class Author(models.Model):
	name=models.CharField(max_length=64,primary_key=True)
	email=models.CharField(max_length=64)

	def __str__(self):
		return "%s (%s)" %(self.name , self.email)

class Post(models.Model):
	title = models.CharField(max_length=64)
	date = models.DateTimeField(null=True)
	author = models.ForeignKey(Author,null=True)
	body = models.TextField()
 
	def __str__(self):
		return "%s (%s)" % (self.title, self.author.name)