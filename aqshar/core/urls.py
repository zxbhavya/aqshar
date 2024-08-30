from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalogue, name='catalog'),
    path('signup/', views.signup, name='signup'),
    path('account/', views.account, name='account'),
    path('sell/', views.selling, name='selling'),
    path('donate/', views.donating, name='donating'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('order/', views.orders, name='orders'),
    # path('add_to_cart/', views.add_to_cart, name='add_to_cart')
]  