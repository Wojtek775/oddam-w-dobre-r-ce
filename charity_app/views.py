from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.db.models import Sum

from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView
from charity_app.models import Institution, Donation, Category


class LandingPage(View):

    def get(self, request):
        count_institution = Institution.objects.count()
        institution = Institution.objects.all()
        items = Donation.objects.all()
        count_bags = sum(items.values_list('quantity', flat=True))

        return render(request, 'base.html',
                      {'count': count_institution, 'total': count_bags, "institution": institution})


class AddDonation(LoginRequiredMixin, View):

    def get(self, request):
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        return render(request, 'form.html', context={'categories': categories, 'institutions': institutions})

    def post(self, request):

        user = request.user
        quantity = request.POST.get('bags')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone')
        city = request.POST.get('city')
        zip_code = request.POST.get('postcode')
        pick_up_comment = request.POST.get('more_info')
        institution_id = request.POST.get('institution')
        pick_up_date = request.POST.get('data')
        pick_up_time = request.POST.get('time')
        category_id = request.POST.get('categories')
        donation_new = Donation.objects.create(user_id=user.id, quantity=quantity, address=address,
                                               phone_number=phone_number, city=city,
                                               zip_code=zip_code, pick_up_comment=pick_up_comment,
                                               institution_id=institution_id,
                                               pick_up_date=pick_up_date, pick_up_time=pick_up_time)

        donation_new.save()
        donation_new.categories.add(category_id)
        return redirect('Confirm')



class Login(View):

    def get(self, request):
        return render(request, 'registration/login.html')

    def post(self, request):
        username = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("LandingPage")
        return redirect('Register')


class Register(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        user = User()
        user.first_name = request.POST.get('name')
        user.last_name = request.POST.get('surname')
        user.email = request.POST.get('email')
        user.set_password(request.POST.get('password'))
        user.username = request.POST.get('email')
        user.save()
        return redirect('Login')


class LogOut(View):
    def get(self, request):
        logout(request)
        return redirect('LandingPage')


class ConfirmView(View):
    def get(self, request):
        return render(request, "form-confirmation.html")
