from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # ex: /comments/5/
    path("<int:comment_id>/", views.detail, name="detail"),
    # ex: /comments/5/results/
    path("<int:comment_id>/update/", views.update, name="update"),
    # ex: /comments/5/vote/
    path("<int:comment_id>/vote/", views.vote, name="vote"),
]