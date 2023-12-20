from django.http import HttpResponse
from . models import Comment
from django.http import JsonResponse
from django.core.serializers import serialize

# Create your views here.

#views.py index => views.index
def index(request):
    #gets list by most recently added up to 5
    serialized_comments = []
    print("REQUEST ***********",request)
    latest_comment_list = Comment.objects.order_by("-date")
    for comment in latest_comment_list:
        serialized_comments.append(comment.serialize())
    print("latest_comment_list", serialized_comments[1])
    return JsonResponse({"comments": serialized_comments})

def detail(request, comment_id):
    return HttpResponse("You're looking at comment %s." % comment_id)

def update(request, comment_id):
    response = "You're looking at the results of comment %s."
    return HttpResponse(response % comment_id)


def vote(request, comment_id):
    return HttpResponse("You're voting on comment %s." % comment_id)