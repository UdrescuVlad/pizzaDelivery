from django.contrib.auth.views import LoginView, LogoutView
from django.http.response import HttpResponse as HttpResponse
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class Login(LoginView):
    template_name = 'userManagement/customLoginTemplate.html'
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('homepage'))
        return super().dispatch(request, *args, **kwargs)
        
class Logout(LoginRequiredMixin, LogoutView):
    login_url = '/user/login/'
    redirect_field_name = "redirect_to"
    template_name = 'userManagement/customLogoutTemplate.html'

class Register(CreateView):
    form_class = UserCreationForm
    template_name = 'userManagement/customRegisterTemplate.html'
    success_url = reverse_lazy('login.page')

    def dispatch(self, request: HttpRequest, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('homepage'))
        return super().dispatch(request, *args, **kwargs)