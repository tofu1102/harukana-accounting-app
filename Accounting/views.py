from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
import time
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .optimizedAccounting import *
from .forms import *
from .models import *
from accounts.models import CustomUser as user

class IndexView(generic.ListView):
    model = event
    template_name = 'Accounting/index.html'

    def get_queryset(self):
        if self.request.user.id != None:
            return event.objects.filter(Member = self.request.user).order_by("id")
        else:
            return None

@login_required
def DetailView(request,event_id):
    Event = get_object_or_404(event,pk = event_id)
    Members = Event.Member.all()
    form = addPayForm(Event,request.POST)

    if "delete" in request.POST:
        Pay = Event.pay_set.get(pk = request.POST['delete'])
        Pay.delete()

    if form.is_valid():
        try:
            APay = Event.pay_set.create(
                payer = form.cleaned_data["payer"],
                price = int(form.cleaned_data["price"]),
                purpose = form.cleaned_data["purpose"],
                auther = request.user,
                )
            for i in form.cleaned_data["payee"]:
                APay.payee.add(Members.get(username = i))
            APay.save()
        except:
            pass

    pays = Event.pay_set.all().order_by("id")
    #value["A"]["B"]でAがBに払うべき金額を示すような二次元辞書を作る
    value = dict()
    for A in Members:
        valueA = dict()
        for B in Members:
            if A == B:
                valueA[A] = 0
            else:
                sum = 0
                #まずAが立て替えたもの
                for plus in pays.filter(payer = A,payee = B,event = Event):
                    sum = sum - plus.price/len(plus.payee.all())
                for minus in pays.filter(payer = B,payee = A,event = Event):
                    sum += minus.price/len(minus.payee.all())
                valueA[B] = int(sum)
            value[A] = valueA
    #最適化提案のために2次元配列にしておく
    valueList = [list(i.values()) for i in value.values()]
    optimized = optimizedAccounting(valueList)
    #表紙のために辞書化する
    optDict = dict()
    ACount = 0
    for A in Members:
        optDictA = dict()
        BCount = 0
        for B in Members:
            optDictA[B] = optimized[ACount][BCount]
            BCount += 1
        optDict[A] = optDictA
        ACount += 1

    if len(pays)>5:
        more = True
    else:
        more = False
    pays = pays.reverse()[:5]
    context = {
        "event":Event,
        "value":value,
        "optimized":optDict,
        "pays":pays,
        "form":addPayForm(Event),
        "more":more,
    }

    template_name = 'Accounting/detail.html'
    return render(request,template_name,context)



@login_required
def history(request,event_id):
    Event = get_object_or_404(event,pk=event_id)

    if "delete" in request.POST:
        Pay = Event.pay_set.get(pk = request.POST['delete'])
        Pay.delete()

    pays = Event.pay_set.all().order_by("id")
    Menbers = Event.Member.all()
    form = searchHistoryForm(Event,request.POST)
    template_name = 'Accounting/history.html'
    if form.is_valid():
        if form.cleaned_data["payer"]:
            pays = pays.filter(payer = Menbers.get(username = form.cleaned_data["payer"]))
        if form.cleaned_data["payee"]:
            for i in form.cleaned_data["payee"]:
                pays = pays.filter(payee = Menbers.get(username = i))
    context ={
        "event":Event,
        "pays":pays,
        "form":searchHistoryForm(Event),
    }
    return render(request,template_name,context)

@login_required
def createEvent(request):
    form = createEventForm(request.POST)
    if form.is_valid():
        User = user.objects.all()
        newEvent = event(name = form.cleaned_data["name"], creater = request.user)
        newEvent.save()
        for i in form.cleaned_data["member"]:
            newEvent.Member.add(User.get(username = i))
        newEvent.save()

        return redirect("Accounting:index")
    else:
        template_name = 'Accounting/createEvent.html'
        context ={
            "form":createEventForm()
        }
        return render(request,template_name,context)
# Create your views here.
