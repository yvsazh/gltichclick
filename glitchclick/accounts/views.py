from django.shortcuts import render, reverse

from .models import *
from arts.models import *
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse

from .forms import *

def register(request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
			new_user = user_form.save(commit=False)
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.save()
			profile = Profile.objects.create(user=new_user)
			return render(request, 'account/register_done.html', {'new_user': new_user})
	else:
		user_form = UserRegistrationForm()

	return render(request, 'account/register.html', {'user_form': user_form})

def profile(request, user_id):

	profile = Profile.objects.get(user = User.objects.get(id = user_id))
	your_profile = Profile.objects.get(user = request.user)

	print(profile.recomendations)

	return render(request, 'account/profile.html', {'profile': profile, 'your_profile': your_profile})

def edit_profile(request):
	if request.method == 'POST':
		user_form = UserEditForm(instance=request.user, data=request.POST)
		profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			return HttpResponseRedirect( reverse('accounts:profile', args = (request.user.id,)) )
		else:
			return HttpResponse("Invalid nickname")


	else:
		user_form = UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile)
		return render(request, 'account/edit_profile.html', {'profile_form': profile_form, 'user_form': user_form})
		