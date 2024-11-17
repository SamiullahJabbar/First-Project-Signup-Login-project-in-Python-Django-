from django import forms




class user_sign_up(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter your email'}))
    password = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'placeholder': 'Enter your password'}))
    re_password= forms.CharField(max_length=10,widget=forms.TextInput(attrs={'placeholder': 'Enter your re_password'}))

    def clean(self):
        cleaned_data = super().clean()
        val_1=cleaned_data['password']
        val_2=cleaned_data['re_password']
        if val_1 != val_2:
           raise forms.ValidationError('the password does not match:')

class user_login(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your password'}))
