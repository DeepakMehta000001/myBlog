from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect #to redirect
from django.contrib import messages #flash messages to tell success
from .forms import PostForm
from .models import Post
# Create your views here.
#it supports CRUD ... 
#function based views (easy)
#class based views


#lets do the CRUD stuffs

def post_create(request):
	#form = PostForm(request.POST) #will show builtin validation
	form = PostForm(request.POST or None) #good way
	#if request.method=='POST':
	#	print(request.POST.get("content"))
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Successfully Created")
		#message success
		return HttpResponseRedirect(instance.get_absolute_url()) 
	
		
	context ={

		"form":form,
	}
	return render(request,"post_form.html",context)


def post_detail(request,id=None): #id is dynamic parameter passed...
	instance = get_object_or_404(Post,id=id) #dyna param is assigned to this.id
	context = {
		"title": instance.title,
		"instance":instance,
	}
	return render(request,"post_detail.html",context)


def post_list(request):
	queryset = Post.objects.all()
	context = {
			"objects_list":queryset,
			"title":"List"
		}
	#if request.user.is_authenticated(): #if logged in through admin
	#	context = {
	#		"title" : "My User List"
	#	}
    #else:
	#	context = {
	#		"title":"List"
	#	}
	return render(request,"post_list.html",context)


def post_update(request,id=None):
	instance = get_object_or_404(Post,id=id) 
	form = PostForm(request.POST or None,instance = instance) 
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Item Saved")
		return HttpResponseRedirect(instance.get_absolute_url()) #message success
 
	context = {
		"title":instance.title,
		"instance":instance,
		"form" : form,
	}
	return render(request,"post_form.html",context)


def post_delete(request,id=None):
	instance = get_object_or_404(Post,id=id) 
	instance.delete()
	messages.success(request,"Successfully Deleted")
	return redirect("posts:list") 