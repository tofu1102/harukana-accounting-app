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
def SettingView(request,CustomUser_id):
    user = get_object_or_404(CustomUser,pk = CustomUser_id)
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



# Create your views here.
