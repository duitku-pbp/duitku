from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from blog.models import Post, Comment, Upvoter
from django.views.decorators.csrf import csrf_exempt


def get_posts(request):
    posts = Post.objects.all()
    return JsonResponse(
        data=[
            {
                "id": post.pk,
                "title": post.title,
                "upvotes": post.upvotes,
                "first_sentence": post.get_first_sentence(),
                "pub_date": post.pub_date,
                "get_comment_amount": post.get_comment_amount(),
            }
            for post in posts
        ],
        safe=False,
    )


@csrf_exempt
def add_post(request):
    if request.method == "POST":
        Post.objects.create(
            title=request.POST["title"], content=request.POST["content"]
        )
        return HttpResponse()
    raise Http404("Invalid request method")


def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return JsonResponse(
        data={
            "id": post.pk,
            "title": post.title,
            "pub_date": post.pub_date,
            "content": post.content,
            "upvotes": post.upvotes,
            "comments": [
                {
                    "id": comment.pk,
                    "user": comment.user,
                    "content": comment.content,
                    "pub_date": comment.pub_date,
                }
                for comment in post.comment_set.all()
            ],
        }
    )


@csrf_exempt
def add_comment(request, post_id):
    if not request.user:
        raise Http404("You must be logged in to post comments!")
    if request.method == "POST":
        content = request.POST["content"]
        if len(content) == 0:
            raise Http404("Comment should not be empty!")
        post = get_object_or_404(Post, id=post_id)
        post.comment_set.create(
            user=request.user.username,
            content=content,
        )
        return HttpResponse()
    raise Http404("Invalid request method")


@csrf_exempt
def update_comment(request, comment_id):
    if not request.user:
        raise Http404("You must be logged in to post comments!")
    if request.method == "POST":
        comment = get_object_or_404(Comment, id=comment_id)
        if comment.user != request.user.username:
            raise Http404("Invalid user")
        comment.content = request.POST["content"]
        comment.save()
        return HttpResponse()
    raise Http404("Invalid request method")


def delete_comment(request, comment_id):
    if not request.user:
        raise Http404("You must be logged in to post comments!")
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return HttpResponse()
