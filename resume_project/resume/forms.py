from django import forms


class registrationForm(forms.Form):
    username = forms.CharField(
        label='login', max_length=30, min_length=4, required=True,

        widget=forms.TextInput(),
    )
    password = forms.CharField(
        label='password', max_length=30, min_length=8, required=True,

        widget=forms.PasswordInput(),
    )