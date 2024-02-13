
import datetime
import logging
import pathlib
import random

from django.shortcuts import render, get_list_or_404, redirect
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils import timezone
from .models import Recipies, Categories, CategoryRecipe
from django.contrib.auth.models import User
from .forms import *
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.core.files.storage import FileSystemStorage
from werkzeug.security import generate_password_hash, check_password_hash
from django.contrib.auth import authenticate, login
# Create your views here.

recipe_field_mapping = {
'name': 'name',
'description': 'description',
'steps': 'steps',
'cooking_time': 'cooking_time',
'image': 'image',
'author': 'author',
'category': 'category',
}

user_field_mapping = {
'username': 'username',
'password1': 'password',

}

models_dict = {
    'recipe':  Recipies,
    'user': User,
    'author': User,
    'category': Categories,
    'category_recipe': CategoryRecipe,
}


def update_fields(item, form, field_mapping_dict):
    for form_field, model_field in field_mapping_dict.items():
        if form.cleaned_data[form_field]:
            setattr(item, model_field, form.cleaned_data[form_field])

    if form.cleaned_data['image']:
        image = form.cleaned_data['image']
        fs = FileSystemStorage()
        fs.save(image.name, image)
        item.image = image
        
def create_item(item, form, field_mapping_dict, models_dict):
    list_of_data = []
    
    for form_field in field_mapping_dict.keys():
        if form.cleaned_data[form_field]:
            # if form_field == 'author':
            #     model = models_dict.get(form_field)
            #     id = request.user.id
            #     list_of_data.append(id)
            # elif form_field == 'category':
            #     model = models_dict.get(form_field)
            #     id = model.objects.filter(name=form.cleaned_data[form_field][0]).first().id
            #     list_of_data.append(id)
            # else:
                
            list_of_data.append(form.cleaned_data[form_field])
    
    return list_of_data
  
    



def index(request):
    
    result = Recipies.objects.all() 
    if len(result) >=5:
        result = random.choices(result, k=5)
    return render(request, 
                  'index.html', 
                  {'list':result, 
                   
                   })
  
def edit_recipe(request):
    title = 'Форма регистрации'
    desc = 'Заполните информацию о рецепте'
    btn = 'Подтвердить'
    if request.method == 'POST':
        form = UpdateRecipiesForm(request.POST, request.FILES)
        if form.is_valid():
            recipe_name = form.cleaned_data['name']
            recipe = Recipies.objects.filter(name=recipe_name).first()
            if recipe:
                update_fields(recipe, form, recipe_field_mapping)
                recipe.save()
            else:
                # form = RecipiesForm(request.POST, request.FILES)
                # if form.is_valid():
                list_of_data = create_item('recipe', form, recipe_field_mapping, models_dict)
                user = User.objects.filter(pk=request.user.id).first()
                item = Recipies(name=list_of_data[0],
                                description=list_of_data[1],
                                steps=list_of_data[2],
                                cooking_time=list_of_data[3],
                                image=list_of_data[4],
                                author=request.user)
                item.save()
    else:
        form = UpdateRecipiesForm()
        
    return render(request, 'form.html', 
                  {'form': form, 
                   'description': desc, 
                   'button': btn, 
                   'title': title})
            
def success_registration(request):
    return render(request, 'success.html')
        
def recipe(request, recipe_id):
    recipe = Recipies.objects.filter(pk=recipe_id).first()
    steps = recipe.steps.split()
    return render(request, 'recipe.html', {'i': recipe, 'steps': steps})

def create_user(request):
    title = 'Форма регистрации'
    desc = 'Заполните информацию о себе'
    btn = 'Зарегистрироваться'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
            return redirect('login')
    else:
        form = UserCreationForm()
        
    return render(request, 'form.html', 
                  {'form': form, 
                   'description': desc, 
                   'button': btn, 
                   'title': title})
    
    



def my_view(request):
    title = 'Вход'
    btn = 'Войти'
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
     
            else:
                messages.warning(request, f'Неверно введены логин или пароль, попробуйте снова.')
                def my_view(request):

            # user = authenticate(request, username=username, password=password)
            # if user is not None:
            #     login(request, user)
            #     return redirect('index')

            # else:
            #     messages.warning(request, f'Неверно введены логин или пароль, попробуйте снова.')
    else:
        form = AuthenticationForm()    
    return render(request, 'login.html', 
                  {'form': form, 
                   'button': btn, 
                   'title': title})
    
def tester(request):
    users = list(User.objects.all())
    for user in users:
        print(user.username)
        print(user.password)
    return redirect('index')
