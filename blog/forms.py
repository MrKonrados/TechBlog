from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Comment


class CommentForm(forms.ModelForm):
    parent = forms.CharField(widget=forms.HiddenInput(
        attrs={'class': 'parent'}), required=False)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'comment-form'
        self.helper.form_method = 'post'
        self.helper.form_action = '.'
        self.helper.add_input(Submit('submit', 'Wyślij'))

    class Meta:
        model = Comment
        exclude = ["post", ]
        # include = ["__all__"]
