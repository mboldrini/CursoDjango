from django import forms

# novo form baseado no form de criacao de registro padrao do django
from django.contrib.auth.forms import UserCreationForm

# pra verificacao do email unico
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):

	email = forms.EmailField(label='E-mail')

	# verifica se o email e unico
	def clean_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError('E-mail ja cadastrado')
		return email


	def save(self, commit=True):
		user = super(RegisterForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
	



# formulario de edicao de conta
# modelform usa os formularios ja do models
class EditAccountForm(forms.ModelForm):

	def clean_email(self):
		email = self.cleaned_data['email']
		queryset =  User.objects.filter(email=email).exclude(pk=self.instance.pk)
		if queryset.exists():
			raise forms.ValidationError('E-mail ja cadastrado')
		return email

	class Meta:
		model = User
		# campos que eu quero que ele possa editar
		fields = ['username', 'email', 'first_name', 'last_name']