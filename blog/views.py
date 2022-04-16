from django.shortcuts import render

from blog.models import Post

# Create your views here.
def index(request):

    context ={
        'posts':Post.objects.all()
    }
    return render(request,'blog/index.html',context)


def post_details(request,id):

    post = Post.objects.get(id=id)
    context={
        'post':post
    }
    return render(request,'blog/post_details.html',context)