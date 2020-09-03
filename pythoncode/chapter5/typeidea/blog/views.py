from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render

from blog.models import Tag, Post, Category


def post_list(request, category_id=None, tag_id=None):
    tag = None
    category = None

    if tag_id:
        p_list, tag = Post.get_by_tag(tag_id)
    elif category_id:
        p_list, category = Post.get_by_category(category_id)
    else:
        p_list = Post.latest_posts()

    context = {
        'category': category,
        'tag': tag,
        'p_list': p_list,
    }

    return render(request, 'blog/list.html', context=context)


def post_detail(request, post_id=None):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None

    return render(request, 'blog/detail.html', context={'post': post})
