from django import forms

from .models import Image


class ImageForms(forms.ModelForm):

    class Meta:
        model = Image
        exclude = ['user', 'date_created']

    def __init__(self, *args, **kwargs):
        super(ImageForms, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': "form-control"})
