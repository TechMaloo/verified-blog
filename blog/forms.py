from django import forms

from .models import Post, Comment, Feed


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]


class NewFeedForm(forms.ModelForm):
    class Meta:
        model = Feed
        fields = ["title", "content", "image"]



class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]

