# -*- coding: utf-8 -*-

#
# 　　　┏┓　　　┏┓
# 　　┏┛┻━━━┛┻┓
# 　　┃　　　　　　　┃
# 　　┃　　　━　　　┃
# 　　┃　┳┛　┗┳　┃
# 　　┃　　　　　　　┃
# 　　┃　　　┻　　　┃
# 　　┃　　　　　　　┃
# 　　┗━┓　　　┏━┛  Codes are far away from bugs with the animal protecting
# 　　　　┃　　　┃    神兽保佑,代码无bug
# 　　　　┃　　　┃
# 　　　　┃　　　┗━━━┓
# 　　　　┃　　　　　  ┣┓
# 　　　　┃　　　　   ┏┛
# 　　　　┗┓┓┏━┳┓┏┛
# 　　　　　┃┫┫　┃┫┫
# 　　　　　┗┻┛　┗┻┛
#


from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse
from west.models import Character
from django.template.context_processors import csrf


# Create your views here.


def staff(request):

	staff_list =  Character.objects.all()
	staff_str = map(str,staff_list)

	return HttpResponse('<p>'+ '--'.join(staff_str) +'</p>')


def first_page(request):

	return HttpResponse('<p>西餐</p>')


def templay(request):

	context = {}
	context['label'] = 'hello world'
	
	return render(request,'templay.html',context)

def templay_staff(request):
	
	staff_list =  Character.objects.all()
	staff_str = map(str,staff_list)
	context = {'label':'--'.join(staff_str)}
	
	return render(request,'templay.html',context)

def templay_code(request):
	
	staff_list =  Character.objects.all()
	context = {'staffs':staff_list,'label':'test-for','numberage':90,'label2':'test-if'}
	
	return render(request,'templay_code.html',context)

def templay_base(request):
	
	staff_list = Character.objects.all()
	context = {'staffs':staff_list}

	return render(request,'templay_base.html',context)

def get_form(request):

	context = {'ht_title':'show form','ht_action':'showform'}

	return render(request,'get_form.html',context)

def investigate_get(request):
	
	rlt = request.GET['staffs']
	context = {'ht_title':'show value','ht_action':'showvalue','staffs':rlt}

	return render(request,'get_form.html',context)

def post_form(request):
	
	ctx = {}
	ctx.update(csrf(request))


	print '+++++++++++++++++++++'
	print request.scheme
	print request.body
	print request.path
	print request.path_info
	print request.method
	print request.encoding
	print request.GET
	print request.POST
	print request.META
	print request.user
	print request.session
	print request.resolver_match
	print request.get_full_path
	print request.build_absolute_uri()
	print request.readline()

	print '---------------------'

	if request.POST:
		ctx['staffs'] = request.POST['staffs']
		context = {'ht_title':'show value','ht_action':'showvalue','staffs':ctx['staffs']}
	else:
		context = {'ht_title':'show form','ht_action':'showform'}

	return render(request,'post_form.html',context)


from django import forms
class CharacterForm(forms.Form):
	name  = forms.CharField(max_length = 200)


def post_db(request):
	
	ctx = {}
	ctx.update(csrf(request))

	print '+++++++++++++++++++++'
	print request.scheme
	print request.body
	print request.path
	print request.path_info
	print request.method
	print request.encoding
	print request.GET
	print request.POST
	print request.META
	print request.user
	print request.session
	print request.resolver_match
	print request.get_full_path
	print request.build_absolute_uri()
	print request.readline()

	print '---------------------'

	if request.POST:

		ctx['staffs'] = request.POST['staffs']
		newrecord = Character(name = ctx['staffs'])
		newrecord.save()

		staff_list = Character.objects.all()

		form = CharacterForm()

		
		context = {'ht_title':'show value','ht_action':'showvalue','staffs':staff_list,'pythonform':form}
	else:
		form = CharacterForm()

		staff_list = Character.objects.all()
		context = {'ht_title':'show form','ht_action':'showform','staffs':staff_list,'pythonform':form}


	return render(request,'post_db.html',context)



from django.contrib import auth


def login(request):
	ctx = {}

	ctx.update(csrf(request))


	if request.POST:
		username = password = ''
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username = username,password = password)

		if user is not None and user.is_active:

			auth.login(request,user)
			return redirect('/')#redirect('/west/post_db')
		else:
			context = {'ht_title':'login_error'}
			return render(request,'login.html',context)

	else:
		context = {'ht_title':'login'}
	

	return render(request,'login.html',context)


def logout(request):
	ctx = {}
	ctx.update(csrf(request))

	return redirect('/west')




