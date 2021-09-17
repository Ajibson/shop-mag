from django import forms

from .models import Image


class ImageForms(forms.ModelForm):

    class Meta:
        model = Image
        exclude = ['user', 'date_created']

    def __init__(self, *args, **kwargs):
        super(ImageForms, self).__init__(*args, **kwargs)
        self.fields['image_name'].widget.attrs.update(
            {"placeholder": "Give your image a name"})
        self.fields['image_category'].widget.attrs.update(
            {"placeholder": "Give your image a name"})
        self.fields['amount_made'].widget.attrs.update({"readonly": "True"})
        self.fields['number_of_download'].widget.attrs.update(
            {"readonly": "True"})
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': "form-control"})
