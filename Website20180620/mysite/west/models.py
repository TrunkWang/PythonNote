# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length=200)
	age = models.IntegerField(default = 0)
	email = models.EmailField()
	def __unicode__(self):
		return self.name

class Tag(models.Model):
	Contact = models.ForeignKey(Contact)
	name = models.CharField(max_length=50)
	def __unicode__(self):
		return self.name


class Character(models.Model):
	name = models.CharField(max_length=200)
	def __unicode__(self):
		return self.name

