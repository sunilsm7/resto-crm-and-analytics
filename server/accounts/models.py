from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE , related_name="user_profile")
	role = models.CharField(max_length=120)
	activated = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'User: {self.user} Role: {self.role}'