from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
#MVC MODEL VIEW CONTROLLER 

#auto_now means every single time its saved in the db, it is set.
#timestamp meaning the first time it is saved in the db(initially)..


class Post(models.Model):
	title = models.CharField(max_length=150)
	image = models.FileField(null=True,blank=True)
	content = models.TextField()
	updated = models.DateTimeField(auto_now =True, auto_now_add=False) 
	timestamp = models.DateTimeField(auto_now =False, auto_now_add=True) 

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("posts:detail",kwargs={"id":self.id})
		#return "/posts/%s/" %(self.id)

	class Meta:
		ordering =["-timestamp","-updated"] #recent first...ordering