from .models import Comment
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class BlogForm(forms.ModelForm):
    conent = forms.CharField(widget=SummernoteWidget())

# While rendering the content in templates use the safe filter which prevents HTML from escaping.
#
# {{ content | safe }}
