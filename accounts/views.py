# adicionei o redirect
from django.shortcuts import render, redirect

#pra adicionar o LOGIN_URL la em baixo
from django.conf import settings

# form de cadastro de usuarios
# form de edicao de senha
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

# form de cadastro que eu criei no arquivo forms.py adicionando o email
# form de edicao de usuario
from .forms import RegisterForm, EditAccountForm

#se o usuario se cadastrar, ja loga ele
from django.contrib.auth import authenticate, login

# os decorators pra so autorizar se o usuario estiver logado
from django.contrib.auth.decorators import login_required



def register(request):
	template_name = 'accounts/register.html'

	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			# se deu certo, ja salva e loga o cara
			user = form.save()
			user = authenticate(
				username=user.username, 
				password=form.cleaned_data['password1']
				)
			login(request, user)
			return redirect( 'core:home' )
	else:
		form = RegisterForm()

	context = {
		'form': form
	}

	return render(request, template_name, context)



@login_required
def dashboard(request):
	template_name = 'accounts/dashboard.html'
	return render(request, template_name)


@login_required
def edit(request):
	template_name = 'accounts/edit.html'
	context = {}
	if request.method == 'POST':
		form = EditAccountForm( request.POST, instance=request.user )
		if form.is_valid():
			form.save()
			form = EditAccountForm( instance=request.user )
			context['success'] = True
	else:
		form = EditAccountForm( instance=request.user )
	context['form'] = form
	return render( request, template_name, context )


@login_required
#edicao de senha ja pronta do django
def edit_password(request):
	template_name = 'accounts/edit_password.html'
	context = {}
	if request.method == 'POST':
		form = PasswordChangeForm( data=request.POST, user=request.user )
		if form.is_valid():
			form.save()
			context['success'] = True
	else:
		form = PasswordChangeForm( user=request.user )
	context['form'] = form
	return render( request, template_name, context )
