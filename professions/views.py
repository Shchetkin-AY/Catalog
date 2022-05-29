from django.shortcuts import redirect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, FormView

from professions.models import Direction, Profile, UserDirect, UserProf
from professions.forms import UserCreationForm, UserDirectionForm


# страница регистрации
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
    next_page = 'catalog'


# страница каталога
class Catalog(LoginRequiredMixin, FormView):
    template_name = 'professions/catalog.html'
    model = Direction
    form_class = UserDirectionForm

    # передаем данные в шаблон каталога
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['direction_list'] = Direction.objects.all()
        context['profile_list'] = Profile.objects.all()
        context['user_dir'] = UserDirect.objects.filter(user_id=self.request.user.id).order_by('directionIndex')
        context['user_prof'] = UserProf.objects.filter(user_id=self.request.user.id).order_by('profileIndex')
        return context

    # НЕ получает данные от catalog ajax
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = request.POST.get('data')
            post = UserDirect(direct_id=1, user_id=request.user.id)
            post.save()
            return redirect('catalog')

    # как вариант попробовать

    #     form = self.form_class(request.POST)
    #
    #     if form.is_valid():
    #         direction = form.save(commit=False)
    #         direction.user_id = request.user.id
    #         direction.direction_id = request.pk
    #         direction.save()
    #         return redirect('favorites')
    #     return self.render_to_response(self.get_context_data(form=form))
