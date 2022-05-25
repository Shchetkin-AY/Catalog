from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView, TemplateView, ListView


from professions.models import Direction, Profile, User, UserDirect, UserProf
from professions.forms import LoginUserForm, UserCreationForm


class RegisterUserView(CreateView):
    template_name = 'professions/registr.html'
    form_class = UserCreationForm
    success_url = 'login'

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return redirect('login')
        return super(RegisterUserView, self).form_valid(form)

# страница аутентификации пользователя
class LoginUserView(LoginView):
    template_name = 'professions/login.html'
    next_page = 'content'


class MainView(LoginRequiredMixin, TemplateView):
    template_name = 'professions/index.html'
    model = Direction

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['direction_list'] = Direction.objects.all()
        context['profile_list'] = Profile.objects.all()
        context['user_dir'] = UserDirect.objects.filter(user_id=self.request.user.id)
        context['user_prof'] = UserProf.objects.filter(user_id=self.request.user.id)
        return context


class Favorites(LoginRequiredMixin, TemplateView):
    template_name = 'professions/test.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['direction_list'] = Direction.objects.all()
        context['profile_list'] = Profile.objects.all()
        context['user_dir'] = UserDirect.objects.filter(user_id=self.request.user.id)
        context['user_prof'] = UserProf.objects.filter(user_id=self.request.user.id)
        return context


    def post(self, request, *args, **kwargs):
        if not request.session.get('favorites'):
            request.session['favorites'] = list()
        else:
            request.session['favorites'] = list(request.session['favorites'])

        item_exist = next((item for item in request.session['favorites'] if item ['type'] == request.POST.get('type') and item['id'] == id), False)

        add_data ={
            'type': request.POST.get('type'),
            'id': id,
        }

        if not item_exist:
            request.session['favorites'].append(add_data)
            request.session.modified = True
        return redirect(request.POST.get('favorites'))