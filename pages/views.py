from django.views import generic
from accounts.models import CustomUser


class HomeView(generic.TemplateView):
    template_name = 'home.html'


class AboutusView(generic.TemplateView):
    template_name = 'pages/aboutus.html'


class ContactusView(generic.TemplateView):
    template_name = 'pages/contactus.html'


class UserListView(generic.ListView):
    queryset = CustomUser.objects.all().order_by('username')
    template_name = 'pages/userlist.html'
    context_object_name = 'users'

class FirstPageView(generic.TemplateView):
    template_name = 'firstpage.html'