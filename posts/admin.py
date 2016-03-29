from django.contrib import admin
#https://docs.djangoproject.com/en/1.9/ref/contrib/admin/
# Register your models here.
from .models import Post 

class PostModelAdmin(admin.ModelAdmin): #modeladmin is referring to the model
	list_display = ['title','updated','timestamp']
	list_display_links =['updated']
	list_editable = ['title']
	list_filter = ['updated','timestamp'] #introduces filtering options for updated and timestamp
	search_fields = ['title','content'] #introduces s search fiel with can search by title and the content of posts.
	class Meta:
		model = Post #this now connects PostModel to PostModelAdmin


admin.site.register(Post,PostModelAdmin)#this will connect Post to admin..


#crud is something how your app works with db