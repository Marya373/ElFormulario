from django.urls import path, include
from recipies import views
from .views import *
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('<int:recipe_id>/', recipe, name='recipe'),
    path('edit/', edit_recipe, name='edit_recipe'),
    path('accounts/register/', create_user, name='create_user'),
    path('accounts/login/', my_view, name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]
