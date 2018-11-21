from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .forms import CustomUserCreationForm

# Create your views here.
class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class PasswordReset(generic.CreateView):
    template_name='password_reset.html'