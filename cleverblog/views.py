from django.shortcuts import render,render_to_response
import  datetime
# Create your views here.
from cleverblog.models import *
from cleverblog.forms import CommentForm
from django.http import Http404
def get_blogs(request):
    blogs = Blog.objects.all().order_by('-created')
    print(blogs)
    #通过键值对来调用{name:content}
    return render_to_response('blog_list.html',{'blogs':blogs})


def get_details(request,blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        raise Http404
    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)
    ctx = {
        'blog':blog,
        'comments':blog.comment_set.all().order_by('-created'),
        'form':form
    }
    return render(request,'blog_details.html',ctx)
def index(request):
    return render(request,'index.html')
def edit(request):
    return render(request,'edit.html')
def edit_action(request):
    print(1)
    title=request.POST.get('title')
    author=request.POST.get('author')
    content=request.POST.get('content')
    Blog.objects.create(title=title,content=content,author=author,catagory=Catagory.objects.get(name='历史'),tags=Tag.objects.get(name='django'),created=datetime.datetime.now())
    blogs = Blog.objects.all().order_by('-created')
    return render_to_response('blog_list.html', {'blogs': blogs})
    print(1)