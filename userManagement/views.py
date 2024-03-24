from typing import Any
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy

class Login(LoginView):
    template_name = 'userManagement/customLoginTemplate.html'
    def dispatch(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('homepage'), context)
        return super().dispatch(request, *args, **kwargs)
        
class Logout(LogoutView):
    template_name = 'userManagement/customLogoutTemplate.html'