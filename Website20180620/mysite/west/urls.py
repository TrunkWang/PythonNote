#!/usr/bin/env python
#-*- coding:utf-8 -*-


from django.conf.urls import include,url
from django.contrib import admin
from west import views


urlpatterns = [
	url(r'^admin/',admin.site.urls),
	url(r'^$',views.first_page),
	url(r'^staff/',views.staff),
	url(r'^templay/',views.templay),
	url(r'^templay_staff/',views.templay_staff),
	url(r'^templay_code/',views.templay_code),
	url(r'^templay_base/',views.templay_base),
	url(r'^get_form/',views.get_form),
	url(r'^investigate_get/',views.investigate_get),
	url(r'^post_form/',views.post_form),
	url(r'^post_db/',views.post_db),
	url(r'^login/',views.login),
	url(r'^logout/',views.logout),
	

]





