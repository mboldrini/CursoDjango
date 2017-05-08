from django.db import models

#model customizado de usuario, baseado no model original do django
# UserManager e o manager, cria superuser, etc
from django.contrib.auth.models import AbstractBaseUser, PermissionsMinix, UserManager


class User(AbstractBaseUser, PermissionsMinix):

	username = models.Charfield('Nome de Usuario', max_length=30, unique=True)
	email = models.EmailField('E-mail', unique=True)
	name = models.Charfield('Nome', max_length=100, blank=True)
	is_active = models.BooleanField('Esta Ativo?', blank=True, default=True)
	is_staff = models.BooleanField('E da equipe', blank=True, default=False)
