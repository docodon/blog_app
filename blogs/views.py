from django.shortcuts import render
from blogs.models import Post,Author
from blogs.forms import BLOGENTRY
from django.utils import timezone


def index(request) :
	all_posts=Post.objects.all().order_by('-date')
	template_data={'posts':all_posts}

	return render(request,'index.html',template_data)


def add_blog(request) :
	if request.method=='POST':
			form=BLOGENTRY(request.POST)
			if form.is_valid() :
				form=form.cleaned_data
				a,b=Author(),Post()
				
				a.name,a.email=form['name'],form['email']
				
				if Author.objects.filter(email = form['name'] , name=form['name']).count() == 0 :
					a.save() 

				b.title=form['title']
				b.date=timezone.now()
				b.author=a
				b.body=form['blog']
				b.save()

			return index(request)
	
	else :
		form=BLOGENTRY()
		
		return render(request,'add_blog.html',{'form':form})
	