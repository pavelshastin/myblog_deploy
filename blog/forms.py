from django import forms


class RegisterForm(forms.Form):

    username = forms.CharField(max_length=100, required=True, label=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(required=True, label=False,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))
    password2 = forms.CharField(required=True, label=False,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password Again', 'class': 'form-control'}))
    email = forms.EmailField(required=True, label=False,
                             widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, label=False, required=False,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, label=False, required=False,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        pswd = cleaned_data["password"]
        pswd2 = cleaned_data["password2"]

        if pswd != pswd2:
            raise forms.ValidationError("Passwords in two fields are not equal", code="invalid")


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True, label=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(required=True, label=False,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))


class CommentForm(forms.Form):
    comment = forms.CharField(required=True, label=False,
                                widget=forms.Textarea(attrs={'cols': '80', 'rows': '4'}))