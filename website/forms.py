from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignupForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
        def __init__(self, *args, **kwargs):
            super(SignupForm, self).__init__(*args, **kwargs)

            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['username'].widget.attrs['placeholder'] = 'Username'
            self.fields['username'].label = ''
            self.fields['username'].help_text = '<ul class="form-text text-muted small"><li>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</li><li>A username must start with a letter.</li></ul>'

            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['placeholder'] = 'Password'
            self.fields['password1'].label = ''
            self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Required. 8 characters or more. </li><li>Contains at least 1 letter and 1 number.</li></ul>'
            
            self.fields['email'].widget.attrs['class'] = 'form-control'
            self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
            self.fields['email'].label = ''
            self.fields['email'].help_text = '<ul class="form-text text-muted small"><li>Required. Inform a valid email address.</li></ul>'


# Create Add record Form
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':"First Name", "class":"form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':"Last Name", "class":"form-control"}), label="")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':"Email", "class":"form-control"}), label="")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':"Phone", "class":"form-control"}), label="")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':"Address", "class":"form-control"}), label="")
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':"City", "class":"form-control"}), label="")
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':"State", "class":"form-control"}), label="")
    zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':"Zipcode", "class":"form-control"}), label="")

    # To designate what model we wanna use.
    class Meta:
        model = Record
        exclude = ("user",)
