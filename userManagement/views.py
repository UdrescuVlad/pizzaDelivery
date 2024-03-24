from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
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