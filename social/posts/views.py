from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Posts, Rating
from django.template import loader
from django.urls import reverse

# GET Posts and .
def index(request):
    # return HttpResponse('HELLO WORLD')
    latest_posts_list = Posts.objects.order_by('-created_at')
    context = {'latest_posts_list': latest_posts_list}

    return render(request, 'posts/index.html', context)


# Show specific post

def detail(request, post_id):
    try:
        post = Posts.objects.get(pk=post_id)
    except Posts.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'posts/detail.html', { 'post': post })


# Get post and display results
def results(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)
    return render(request, 'posts/results.html', { 'post': post })


#  Vote for a choice
def vote(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)
    # print('REQUEST:::', request.POST['like'])
    
    if( 'like' in request.POST ):
        selected_like = post.rating_set.get(pk=int(request.POST['like']))
        selected_like.likes += 1
        selected_like.save()
        print(selected_like)
    elif ('dislike' in request.POST):
        selected_dislike = post.rating_set.get(pk=int(request.POST['dislike']))
        selected_dislike.dislikes += 1
        selected_dislike.save()
        print(selected_dislike)
    return HttpResponseRedirect(reverse('posts:results', args=(post.id,)))