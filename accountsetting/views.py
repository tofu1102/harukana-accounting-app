from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
import time
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .forms import *
from accounts.models import CustomUser

@login_required
def SettingView(request):
    user = request.user
    errorText = None

    form = CustomUserSettingForm(user,request.POST)

    if form.is_valid():
        if CustomUser.objects.filter(username = form.cleaned_data["username"]).exists():
            errorText = "そのユーザーネームはすでに使われています"
        else:
            user.username = form.cleaned_data["username"]
            user.save()
            return redirect("Accounting:index")

    template_name = 'accountsetting/UserSetting.html'
    context = {
        "form":CustomUserSettingForm(user),
        "errorText":errorText
    }
    return render(request,template_name,context)

@login_required
def friend(request):
    user = request.user
    errorText = None
    resultUser = None

    if "makefriends" in request.POST:
        another = CustomUser.objects.filter(id = request.POST["makefriends"])[0]
        user.friend.add(another)
        another.friend.add(user)
        errorText = "登録しました。"

    form = searchCustomUserForm(request.POST)

    if form.is_valid():
        if CustomUser.objects.filter(id = form.cleaned_data["id"],is_active = True).exists():
            resultUser = CustomUser.objects.filter(id = form.cleaned_data["id"],is_active = True)[0]
        else:
            errorText = "idに一致するユーザーは存在しません。"
    template_name = 'accountsetting/makefriends.html'
    context = {
        "form":searchCustomUserForm(),
        "errorText":errorText,
        "resultUser":resultUser,
    }
    return render(request,template_name,context)



# Create your views here.
