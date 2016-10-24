from __future__ import unicode_literals

from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Secret(models.Model):
	content = models.CharField(max_length=500)
	postDate = models.DateTimeField('date posted')
	user = models.ForeignKey(User)
	def __unicode__(self):
		return self.content
