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


#  Vote for a question choice
def vote(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)
    try:
        selected_like = post.rating_set.get(pk=request.POST['like'])
        print(selected_like)
        selected_dislike = post.rating_set.get(pk=request.POST['dislike'])
    except (KeyError, Rating.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'posts/detail.html', {
            'post': post,
            'error_message': "You didn't select anything.",
        })
    else:
        if(selected_like):
           selected_like.likes += 1
           selected_like.save()
        else:
            selected_dislike += 1 
            selected_dislike.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('posts:results', args=(post.id,)))