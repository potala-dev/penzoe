from django import forms


class BookUploadForm(forms.Form):
    title = forms.CharField(max_length=250)
    author = forms.CharField(max_length=100)
    file = forms.FileField()
