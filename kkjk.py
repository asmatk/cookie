from cookie.blog.models import Post


def h():
    Post.objects.all()
    return
