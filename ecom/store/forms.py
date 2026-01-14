from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from.models import Product


class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''


class ProductForm(forms.ModelForm):
	class Meta:
		model= Product
		fields= '__all__'
		widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Product name'
            }),

            'price': forms.NumberInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Price'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control mb-3',
                'rows': 4,
                'placeholder': 'Product description'
            }),

            'category': forms.Select(attrs={
                'class': 'form-select mb-3'
            }),

            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control mb-3'
            }),
		}
			