from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post


def post_list(request):
  posts = Post.published.all()

  paginator = Paginator(posts, 2) # 10 posts in each page
  page = request.GET.get('page')
  try:
    posts = paginator.page(page)
  except PageNotAnInteger:
    # If page is not an integer deliver the first page
    posts = paginator.page(1)
  except EmptyPage:
    # If page is out of range deliver last page of results
    posts = paginator.page(paginator.num_pages)

  return render(request,'post_list.html',{'posts':posts})


def post_detail(request, post):
  post=get_object_or_404(Post,slug=post,status='published')
  return render(request, 'post_detail.html',{'post':post})
