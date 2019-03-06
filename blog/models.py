from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import CustomUser


class Post(models.Model):
	author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=0)
	title = models.CharField(max_length=200)
	text = models.TextField()
	price = models.IntegerField(null=True, blank=False, validators=[MinValueValidator(1),MaxValueValidator(999999)])
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	image = models.ImageField(null=True, blank=False)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title	