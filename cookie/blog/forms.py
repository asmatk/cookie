from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):

    # def clean(self):
    #     cleaned_data = super(PostForm, self).clean()
    #     title = cleaned_data['title']
    #     if not title.endswith('asma'):
    #         raise ValidationError('please add asma to the title')
    #     return cleaned_data

    class Meta:
        model = Post
        fields = ('title', 'text', 'created_date',)




# class PostForm(forms.Form):
#     name = forms.CharField()
#     title = forms.CharField()
#     text = forms.CharField(widget=forms.Textarea)
#     message = forms.CharField(widget=forms.Textarea)
#
#     # created_date = forms.DateField()
#     def send_email(self):
#         # send email using the self.cleaned_data dictionary
#         pass
