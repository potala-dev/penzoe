from django import forms

GENRE_CHOICES = [
    ("buddhism", "Buddhism"),
    ("finance", "Finance"),
    ("fiction", "Fiction"),
    ("history", "History"),
    ("politics", "Politics"),
    ("self-help", "Self-Help"),
    ("other", "Other"),
]


class BookUploadForm(forms.Form):
    title = forms.CharField(max_length=250)
    author = forms.CharField(max_length=100)
    genre = forms.ChoiceField(choices=GENRE_CHOICES)
    file = forms.FileField()
