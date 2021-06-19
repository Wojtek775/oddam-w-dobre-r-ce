from django.db.models import Sum
from django.shortcuts import render

# Create your views here.
from django.views import View

from charity_app.models import Institution, Donation


class LandingPage(View):

    def get(self, request):
        count_institution = Institution.objects.count()
        items = Donation.objects.all()
        count_bags = sum(items.values_list('quantity', flat=True))

        return render(request, 'base.html', {'count': count_institution, 'total': count_bags})


class AddDonation(View):

    def get(self, request):
        return render(request, 'form.html')


class Login(View):

    def get(self, request):
        return render(request, 'login.html')


class Register(View):
    def get(self, request):
        return render(request, 'register.html')
