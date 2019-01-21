from django.forms import ModelForm
from .models import Post
from .models import Comment

class PostModelForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['id']
        exclude = ['date_updated']
        exclude = ['is_active']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['id']
        exclude = ['date_created']
