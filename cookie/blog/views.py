from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import PostForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy, reverse
from cookie.blog.models import Author
from django.contrib.auth.decorators import login_required


# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'blog/post_list.html', {'posts': posts})
#

class ListPostView(LoginRequiredMixin, ListView):
    template_name = 'blog/post_list.html'
    queryset = Post.objects.filter(published_date__lte=timezone.now())
    context_object_name = 'posts'


# def post_detail(request, **kwargs):
#     # print('THE REQUEST IS:', type(request.user))
#     messages.error(request, 'see details deleted.')
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})


class DetailPostView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             article = form.save(commit=False)
#             article.author = request.user
#             article.published_date = timezone.now()
#             article.save()
#             return redirect('post_detail', pk=article.pk)
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})

class PostCU(object):

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})


class NewPostView(LoginRequiredMixin, PostCU, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'blog/post_edit.html'

    def form_valid(self, form):
        article = form.save(commit=False)
        article.author = self.request.user
        article.published_date = timezone.now()
        # send email
        return super(NewPostView, self).form_valid(form)


class EditPostView(LoginRequiredMixin, PostCU, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'blog/post_edit.html'


# def post_edit(request, pk):
#     article = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=article)
#         if form.is_valid():
#             article = form.save()
#             return redirect('post_detail', pk=article.pk)
#     else:
#         form = PostForm(instance=article)
#     return render(request, 'blog/post_edit.html', {'form': form})


'''second method for edit (update)'''

# class EditPostView(UpdateView):
#     model = Post
#     fields = ['title', 'text', 'created_date']
#     template_name = 'blog/post_edit.html'
#
#     def form_valid(self, form_class, pk):
#         article = form_class.save()
#         return redirect('post_detail', pk=article.pk)
#
#     def form_invalid(self, form_class, pk):
#         article = get_object_or_404(Post, pk=pk)
#         form = PostForm(instance=article)
#         form.as_p()
#         return HttpResponse('please check your data')
#
#     def post(self, request, pk, *args, **kwargs):
#         article = get_object_or_404(Post, pk=pk)
#         print('the value of the pk is : ', pk)
#         print('the value of the request is : ', request)
#         print('the value of the *args is : ', *args)
#         print('the value of the **kwargs is : ', **kwargs)
#
#         if request.method == "POST":
#             form = PostForm(request.POST, instance=article)
#             if form.is_valid():
#                 article = form.save()
#                 return redirect('post_detail', pk=article.pk)
#         else:
#             form = PostForm(instance=article)
#             form.as_p()
#         return render(request, 'blog/post_edit.html', {'form': form})


'''edit with FormView class'''

# class EditPostView(FormView):
#     form_class = PostForm
#     template_name = 'blog/post_edit.html'
#     # context_object_name = 'post'
#
#     def get_initial(self):
#         return {'title': 'ww', 'text': 'qwerty'}
#
#     # def form_valid(self, form_class, pk):
#     #     article = form_class.save()
#     #     return redirect('post_detail', pk=article.pk)
#     #
#     #
#     #
#     # def form_invalid(self, form_class, pk):
#     #     article = get_object_or_404(Post, pk=pk)
#     #     form = PostForm(instance=article)
#     #     form.as_p()
#     #     return render(request, 'blog/post_edit.html', {'form': form})


'''this is the part one of the tuto of changement '''


# class PostView(FormView):
#     template_name = 'post_list.html'
#     form_class = PostForm
#     success_url = '/thanks/'
#
#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         form.send_email()
#         return super().form_valid(form)


class AuthorCreate(CreateView):
    model = Author
    fields = ['name']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get(self, request):
        return HttpResponse('it s ok')


class AuthorUpdate(UpdateView):
    model = Author
    fields = ['name']


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('author-list')


class GreetingView(View):
    greeting = "Good Day"

    def get(self, request):
        return HttpResponse(self.greeting)
