from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required     # login decorator
from django.contrib import messages
from django.core.paginator import Paginator
from .models import *
from .forms import *


score = 0
count = 0


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm() #we imorted it above from forms
        # now we will process this form
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user_pro = form.save()
                Profile.objects.create(anna=user_pro)
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'namo/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'namo/login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')


def index(request):
    global score
    score = 0
    return render(request, 'namo/index.html')

@login_required(login_url='login')
def languages(request):
    sub = Subject.objects.all()
    context = {'sub': sub}
    return render(request, 'namo/languages.html', context)

@login_required(login_url='login')
def test(request, pk):
    subn = Subject.objects.get(id=pk)
    namn = subn.name
    que = Question.objects.filter(subject__name=subn)
    paginator = Paginator(que, 1)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    context = {'namn': namn, 'question': page_obj}
    return render(request, 'namo/test.html', context)

@login_required(login_url='login')
def saveSelected(request, pk):
    global score
    global count

    if request.method == "POST":
        selected = request.POST['option']
        count += 1
    correct_ans = Question.objects.get(id=pk)
    if (selected == correct_ans.correct):
        score += 1
    return redirect(request.META['HTTP_REFERER'])


@login_required(login_url='login')
def result(request):
    global score
    global count
    context = {'score': score, 'count': count}
    return render(request, 'namo/result.html', context)

@login_required(login_url='login')
def contactus(request):
    return render(request, 'namo/contact.html')

@login_required(login_url='login')
def profile(request):
    profile = Profile.objects.get(anna=request.user)
    context = {'profile': profile}
    return render(request, 'namo/profile.html', context)

@login_required(login_url='login')
def update(request):
    cur_user = Profile.objects.get(anna=request.user)
    form = ProfileForm(instance=cur_user)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=cur_user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    context = {'form': form}
    return render(request, 'namo/updateProfile.html', context)
