from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =['title','body','image']
        widgets = {
            'title': forms.TextInput(attrs={
            'class':'input',
            'placeholder':' Post Title'}),
            'body': forms.Textarea(attrs={
                'class':'input',
                'placeholder':' Post Body'
            })
        }