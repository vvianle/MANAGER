from __future__ import unicode_literals
from datetime import datetime, time
from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin, AbstractBaseUser


class OneUserManager(BaseUserManager):
	def _create_user(self, username, email, password):
		"""
		Creates and saves a User with the given email, date of
		birth and password.
		"""
		now = datetime.now()
		if username is None:
			raise ValueError('Must include username')
		if email is None:
			raise ValueError('The given email must be set')
		email = self.normalize_email(email)

		user = self.model(
			email=self.normalize_email(email),
			username=username,
			date_joined=now
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, username=None, email=None, password=None):
		"""Create and save an EmailUser with the given email and password.
		:param str email: user email
		:param str password: user password
		:return custom_user.models.EmailUser user: regular user
		"""
		return self._create_user(username, email, password)

	def create_superuser(self, username, email, password):
		"""Create and save an EmailUser with the given email and password.
		:param str email: user email
		:param str password: user password
		:return custom_user.models.EmailUser user: admin user
		"""
		user = self._create_user(username, email, password)
		user.is_admin = True
		user.save(using=self._db)
		return user


class AbstractOneUsers(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(max_length=255, unique=True)
	username = models.CharField(max_length=100, unique=True)
	fullname = models.CharField(max_length=255, blank=True, default="")
	date_joined = models.DateTimeField(default=datetime.now, blank=True)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	has_working_schedule = models.BooleanField(default=False, verbose_name='Has working schedule')

	class Meta:
		db_table = "one_users"
		abstract = True

	objects = OneUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	def __str__(self):  # __unicode__ on Python 2
		return self.username

	def get_full_name(self):
		# The user is identified by their email address
		return self.username

	def get_short_name(self):
		# The user is identified by their email address
		return self.username

	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True

	@property
	def is_staff(self):
		"Is the user a member of staff?"
		# Simplest possible answer: All admins are staff
		return self.is_admin


class MyUser(AbstractOneUsers):
	"""
	Concrete class of AbstractEmailUser.
	Use this if you don't need to extend EmailUser.
	"""

	class Meta(AbstractOneUsers.Meta):
		swappable = 'AUTH_USER_MODEL'
