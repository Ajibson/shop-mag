from django import forms
from .models import User, Messages
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class SignUpForm(forms.ModelForm):

    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name',
                  'password']
        widgets = {
            'password': forms.PasswordInput()}

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': "form-control"})
        self.fields['email'].widget.attrs.update({"oninput": "checkemail()"})
        self.fields['password'].widget.attrs.update(
            {"oninput": "checkpassword()"})

    # Do form cleanig here

    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     # confirm_password = self.cleaned_data.get("confirm_password")
    #     if username in [entry.username for entry in User.objects.all()]:
    #         raise ValidationError('Username is not available')
    #     return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email in [entry.email for entry in User.objects.all()]:
            raise ValidationError("Email not available for use")
        return email

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get("confirm_password")
        # check password length
        if password != confirm_password:
            raise ValidationError("Passwords do not match")

        return confirm_password

    def clean_password(self):
        password = self.cleaned_data.get('password')
        # check password length
        if len(password) < 8:
            raise ValidationError("Password can't be less than 8 characters")
        # check for number and letters is password
        if password.isalpha() or password.isnumeric():
            raise ValidationError(
                "Password should contains both letters and numbers")

        return password


""" When name is password it did not read confirm_password and thus the form is not valid
    when name is confirm_password it read both fields and thus the form is valid
"""


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=200)
    password = forms.CharField(max_length=200)


class PasswordChangeForm(forms.Form):
    new_password = forms.CharField(max_length=30)

    def clean_new_password(self):
        new_password = self.cleaned_data.get('new_password')

        # check password length
        if len(new_password) < 8:
            raise ValidationError("Password can't be less than 8 characters")
        # check for number and letters is password
        if new_password.isalpha() or new_password.isnumeric():
            raise ValidationError(
                "Password should contains both letters and numbers")

        return new_password


class ResetForms(forms.Form):
    email = forms.EmailField()


class NewPasswordResetForm(forms.Form):
    # password = forms.CharField(widget=forms.PasswordInput())
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")

        # check password length
        if len(password2) < 8:
            raise ValidationError("Password can't be less than 8 characters")
        # check for number and letters is password
        if password2.isalpha() or password2.isnumeric():
            raise ValidationError(
                "Password should contains both letters and numbers")

        return password2


class MessageForm(forms.ModelForm):

    class Meta:
        model = Messages
        fields = ['message']
