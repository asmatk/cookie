from django.http import HttpResponse
from django.urls import path

from cookie.blog.views import AuthorCreate, AuthorUpdate, AuthorDelete, GreetingView, ListPostView, NewPostView, \
    EditPostView, DetailPostView
from . import views
from django.conf.urls import url


def test():
    return HttpResponse('hello')


# urlpatterns = [
#     path('', views.post_list, name='post_list'),
#     path('post/<int:pk>/', views.post_detail, name='post_detail'),
#     path('post/new/', views.post_new, name='post_new'),
#     path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
#     path('post/call/', test, name='post_edit'),
#
# ]

urlpatterns = [
    path('author/add/', AuthorCreate.as_view(), name='author-add'),
    path('author/<int:pk>/', AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', AuthorDelete.as_view(), name='author-delete'),

    path('about/', GreetingView.as_view(greeting="G'day")),

    path('', ListPostView.as_view(), name='post_list'),
    # path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/detail/<int:pk>/', DetailPostView.as_view(), name='post_detail'),
    # path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/edit/', EditPostView.as_view(), name='post_edit'),
    path('post/new/', NewPostView.as_view(), name='post_new'),

    # DRF
]
