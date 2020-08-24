from crispy_forms.helper import FormHelper
from django import forms


class ThreadForm(forms.Form):
    title = forms.CharField(max_length=200)
    body = forms.CharField(max_length=5000, widget=forms.Textarea, required=False)


class CommentForm(forms.Form):
    text = forms.CharField(
        max_length=5000,
        widget=forms.Textarea(attrs={"placeholder": "Type your comment here."}),
    )

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
