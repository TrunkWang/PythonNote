# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from west.models import Character,Contact,Tag


# Register your models here.
#class ContactAdmin(admin.ModelAdmin):
#	fields = ('name','email')

'''
class TagInline(admin.TabularInline):
	model = Tag


class ContactAdmin(admin.ModelAdmin):
	inlines = [TagInline]
	fieldsets = (['Main',{'fields':('name','email'),}],['Advance',{'classes':('collapse',),'fields':('age',),}])
'''
class ContactAdmin(admin.ModelAdmin):
	list_display = ('name','age','email')
	search_fields = ('name',)


admin.site.register(Contact,ContactAdmin)


admin.site.register([Character,Tag])