from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField (max_length = 250)
	body = models.TextField ()
	date_created = models.DateField (auto_now_add = True)
