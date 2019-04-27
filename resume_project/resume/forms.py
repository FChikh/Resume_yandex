from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label='login', max_length=30, min_length=4, required=True,

        widget=forms.TextInput(),
    )
    password = forms.CharField(
        label='password', max_length=30, min_length=8, required=True,

        widget=forms.PasswordInput(),
    )




class RegistrationForm(forms.Form):
    username = forms.CharField(
        label='login', max_length=30, min_length=4, required=True,

        widget=forms.TextInput(),
    )
    email = forms.EmailField(
        label='email', required=True,

        widget=forms.EmailInput(),
    )
    password = forms.CharField(
        label='password', max_length=30, min_length=8, required=True,

        widget=forms.PasswordInput(),
    )
    re_password = forms.CharField(
        label='password', max_length=30, min_length=8, required=True,

        widget=forms.PasswordInput(),
    )
    agree_term = forms.BooleanField(
        label='terms', required=True,

        widget=forms.RadioSelect(),
    )

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("re_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password and Confirm password does not match"
            )
