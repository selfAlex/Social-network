from django import forms


class SignInForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'uk-input', 'id': 'signin_email'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'uk-input',
                                                                                   'id': 'signin_password'}))


class SignUpForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'uk-input', 'id': 'signup_email'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'uk-input',
                                                                                   'id': 'signup_password'}))


class ProfileEditForm(forms.Form):
    first_name = forms.CharField(label='First name', widget=forms.TextInput(attrs={'class': 'uk-input',
                                                                                   'required': False}))

    surname = forms.CharField(label='Surname', widget=forms.TextInput(attrs={'class': 'uk-input',
                                                                             'required': False}))
