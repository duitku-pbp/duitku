from django.urls import path

from . import views
from . import endpoint_views

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
    path("endpoints/get_posts/", endpoint_views.get_posts, name="endpoint_get_posts"),
    path("endpoints/add_post/", endpoint_views.add_post, name="endpoint_add_post"),
    path("endpoints/<int:post_id>/", endpoint_views.detail, name="endpoint_detail"),
    path(
        "endpoints/add_comment/<int:post_id>/",
        endpoint_views.add_comment,
        name="endpoints_add_comment",
    ),
    path(
        "endpoints/delete_comment/<int:comment_id>/",
        endpoint_views.delete_comment,
        name="endpoint_delete_comment",
    ),
    path(
        "endpoints/update_comment/<int:comment_id>/",
        endpoint_views.update_comment,
        name="endpoint_update_comment",
    ),
]
