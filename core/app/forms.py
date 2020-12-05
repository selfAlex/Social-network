from django import forms


class SignInForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'uk-input', 'id': 'signin_email'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'uk-input',
                                                                                   'id': 'signin_password'}))


class SignUpForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'uk-input', 'id': 'signup_email'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'uk-input',
                                                                                   'id': 'signup_password'}))
