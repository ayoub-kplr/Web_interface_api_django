from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse

from .models import IncomeExpenses


@login_required
def expensesData(request):
    return render(request, "data.html", context={"entries": IncomeExpenses.objects.all()})


def addExpense(request):
    print(request.POST)
    return render(request, template_name="add.html")

def login_request(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return HttpResponseRedirect("/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    form.fields['username'].widget.attrs['class'] = "form-control email"
    form.fields['password'].widget.attrs['class'] = "form-control otp"
    return render(request=request, template_name="login.html", context={"login_form": form})
