from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View
# Create your views here.


class DashboardView(LoginRequiredMixin, View):
    login_url = "account/login"

    def get(self, request):
        ...

