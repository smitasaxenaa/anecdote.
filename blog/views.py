from django.shortcuts import render, get_object_or_404
from .models import Post,Comment
from .forms import PostForm, CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def dashboard(request):
    return render(request, "blog/dashboard.html")

def userposts_list_view(request):

    allposts= Post.objects.all().order_by('-created_on')

    context= {'allposts': allposts,
              }

    return render(request, 'userposts-list-view.html', context)


#detail view
def userposts_detail_view(request, url=None):

    post= get_object_or_404(Post, url=url)
    comments = Comment.objects.filter(post=post)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()


    context= {'post': post,
              "comments": comments,
              "form": form,
              }

    return render(request, 'userposts-detail-view.html', context)
