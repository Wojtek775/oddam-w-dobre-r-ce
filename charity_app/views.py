from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.db.models import Sum
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from charity_app.models import Institution, Donation


class LandingPage(View):

    def get(self, request):
        count_institution = Institution.objects.count()
        institution = Institution.objects.all()
        items = Donation.objects.all()
        count_bags = sum(items.values_list('quantity', flat=True))

        return render(request, 'base.html',
                      {'count': count_institution, 'total': count_bags, "institution": institution})


class AddDonation(View):

    def get(self, request):
        return render(request, 'form.html')


class Login(View):

    def get(self, request):
        return render(request, 'registration/login.html')


class Register(View):
    def get(self, request):
        return render(request, 'register.html')
