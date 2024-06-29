from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from random import choice
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .models import Recipe, Category
from .forms import NewUserForm, LoginForm, NewTemplate
from django.views.generic import CreateView, UpdateView

import logging

logger = logging.getLogger(__name__)

def index(request):
    recipes_all = Recipe.objects.order_by('?')[:5]
    return render(request, 'myapp/index.html', {'recipes_all': recipes_all})


def recipe(request, recipe_id):
    recipe_v = Recipe.objects.get(pk=recipe_id)
    return render(request, 'myapp/recipe.html', {'recipe': recipe_v})


def recipe_detail(request, recipe_id=2):
    recipe_v = Recipe.objects.get(pk=recipe_id)
    return render(request, 'myapp/detail.html', {'recipe': recipe_v})


def list_all(request):
    username = request.user
    recipes_all = Recipe.objects.filter(owner=username)
    return render(request, 'myapp/list_all.html', {'recipes_all': recipes_all})


def publish_new(request):
    if request.method == 'POST':
        form = NewTemplate(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            recipe.owner = request.user
            logger.info(f'{recipe.owner} Added a new recipe !')
            return redirect('index')
    else:
        form = NewTemplate()
    return render(request, 'myapp/publish_new.html', {'form': form})


def edit_recipe(request, recipe_id=2):
    recipe_v = Recipe.objects.get(pk=recipe_id)
    if request.method == 'POST':
        form = NewTemplate(request.POST, request.FILES, instance=recipe_v)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/published.html')
    else:
        form = NewTemplate(instance=recipe_v)
        return render(request, 'myapp/edit_recipe.html', {'form': form})


class RegisterNewView(SuccessMessageMixin, CreateView):
    form_class = NewUserForm
    success_url = reverse_lazy('index')
    template_name = 'myapp/new_user.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New User Registration'
        return context


class UserLoginView(SuccessMessageMixin, LoginView):
    form_class = LoginForm
    template_name = 'myapp/user_login.html'
    next_page = 'index'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'User Login Page'
        return context


class RecipeListView(ListView):
    template_name = 'myapp/list_all.html'
    model = Recipe
    context_object_name = 'recipes_all'


class UserLogoutView(LogoutView):
    next_page = 'index'


class Published(TemplateView):
    template_name = 'myapp/published.html'


class Index(TemplateView):
    template_name = 'myapp/index.html'
