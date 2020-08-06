from django import forms
from .models import Post,Comment

#choices = Category.objects.all().values_list('name','name')

#choice_list = []

#for item in choices:
#    choice_list.append(item)

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )


class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields= ['name','title','field','content']
        widgets = {
        'name' : forms.TextInput(attrs={'class':'form-control'}),
        'title' : forms.TextInput(attrs={'class':'form-control'}),
        'content' : forms.Textarea(attrs={'class':'form-control'}),
        }
