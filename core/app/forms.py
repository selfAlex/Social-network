from django import forms


class SignInForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'uk-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'uk-input'}))


class SignUpForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'uk-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'uk-input'}))

