from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("get_posts/<int:limit>/", views.get_posts, name="get_posts"),
    path("<int:post_id>/", views.detail, name="detail"),
    path("add_post/", views.add_post.as_view(), name="add_post"),
    path("add_post_execute", views.add_post_execute, name="add_post_execute"),
    path(
        "<int:post_id>/<int:comment_id>/edit_comment/",
        views.edit_comment,
        name="edit_comment",
    ),
    path(
        "<int:post_id>/<int:comment_id>/update_comment/",
        views.update_comment,
        name="update_comment",
    ),
    path(
        "<int:post_id>/<int:comment_id>/delete_comment/",
        views.delete_comment,
        name="delete_comment",
    ),
    path("<int:post_id>/post_comment/", views.post_comment, name="post_comment"),
]
