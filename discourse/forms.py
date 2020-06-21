from django import forms


class ThreadForm(forms.Form):
    title = forms.CharField(max_length=200)
    body = forms.CharField(max_length=5000, widget=forms.Textarea, required=False)


class CommentForm(forms.Form):
    body = forms.CharField(max_length=5000, widget=forms.Textarea, required=False)
